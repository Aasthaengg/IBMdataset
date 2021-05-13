import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, k = inintm()

ans = 0

for i in range(1,n+1):
    b = 0
    for _ in range(1,18):
        if i >= k:
            break
        i *= 2
        b += 1
    ans += (1/n)*(0.5**b)

print(ans)
