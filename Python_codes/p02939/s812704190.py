import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
prev = ""
ans = 0
n = len(s)
i = 0
while i<n:
    if s[i]==prev:
        if i+1<n:
            ans += 1
            prev = s[i]+s[i+1]
        i += 2
    else:
        prev = s[i]
        i += 1
        ans += 1
#     print(prev)
print(ans)