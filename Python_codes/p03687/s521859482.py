import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
def sub(c):
    ss = s[:]
    ans = 0
    while True:
        if all(c==ss[i] for i in range(len(ss))):
            break
        ans += 1
        tmp = []
        for i in range(len(ss)-1):
            if c in (ss[i], ss[i+1]):
                tmp.append(c)
            else:
                tmp.append(ss[i])
        ss = "".join(tmp)
    return ans
ans = float("inf")
for c in set(s):
    ans = min(ans, sub(c))
print(ans)