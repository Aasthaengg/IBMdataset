import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
s = input()
t = input()

ans = 10**10

for i in range(n - 1, -1, -1):
    if s[i:] == t[:n-i]:
        if len(s) + len(t[n-i:]) >= n:
            ans = min(ans, len(s) + len(t[n-i:]))
if len(s) + len(t) >= n:
    ans = min(ans, len(s) + len(t))

if ans == 10**10:
    print(n)
else:
    print(ans)