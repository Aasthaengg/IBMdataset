import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = inintl()

ans = 10**6

for a in A:
    cnt = 0
    while a % 2 == 0:
        a /= 2
        cnt += 1
    if cnt < ans:
        ans = cnt

print(ans)
