import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b, c = inintm()

if a == b == c == 1:
    print(0)
    exit()

if a == b == c:
    print(-1)
    exit()

ans = 0

while a % 2 == b % 2 == c % 2 == 0:
    d = a
    e = b
    f = c
    a = e/2 + f/2
    b = d/2 + f/2
    c = d/2 + e/2
    ans += 1

print(ans)