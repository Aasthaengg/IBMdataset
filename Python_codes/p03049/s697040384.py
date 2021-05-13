import sys
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
ans = 0
a=0
b=0
c=0

for i in range(n):
    s = ns()
    ans += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        c += 1
    elif s[0] == 'B':
        b += 1
    elif s[-1] == 'A':
        a += 1

ans += min(n-1,a,b)+c
if a+b == 0 and c > 0:
    ans -= 1

print(ans)
