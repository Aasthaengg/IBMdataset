import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, k = inintm()

h = []
ans = 10**10

for _ in range(n):
    h.append(inint())

h.sort()

for i in range(n-k+1):
    if h[i+k-1] - h[i] < ans:
        ans = h[i+k-1] - h[i]

print(ans)