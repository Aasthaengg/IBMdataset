import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()

m = 0
ans = 1

for i in range(1,n+1):
    if i % 2 == 1:
        continue
    cnt = 0
    t = i
    while t % 2 == 0:
        t //= 2
        cnt += 1
    if cnt > m:
        ans = i
        m = cnt

print(ans)
