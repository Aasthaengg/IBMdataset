import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
n = len(s)
c = 0
ans = 0
for i in range(n):
    if s[i]=="W":
        ans += c
    else:
        c += 1
print(ans)