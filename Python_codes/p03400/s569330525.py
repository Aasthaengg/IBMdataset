import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
d, x = inintm()

ans = 0

for _ in range(n):
    a = inint()
    for i in range(102):
        if a*i + 1 > d:
            break
        ans += 1

print(ans+x)
