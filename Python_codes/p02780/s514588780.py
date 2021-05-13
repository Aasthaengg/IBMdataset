import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, k = inintm()
P = inintl()

s = [0]*(n+1)
ans = 0

for i in range(n):
    s[i+1] = s[i]+(1 + (P[i]-1)*0.5)

for i in range(n-k+1):
    if s[i+k] - s[i] > ans:
        ans = s[i+k] - s[i]

print(ans)