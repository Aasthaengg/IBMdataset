import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, x = inintm()
A = inintl()

A.sort()
ans = 0

for i in range(n-1):
    if x - A[i] >= 0:
        ans += 1
        x -= A[i]

if A[-1] == x:
    ans += 1

print(ans)
