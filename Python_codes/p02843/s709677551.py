import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

x = inint()

res = x % 100
lim = x//100

c = res//5
res %= 5
c += res//4
res %= 4
c += res//3
res %= 3
c += res//2
res %= 2
c += res//1
res %= 1

if lim < c:
    print(0)
else:
    print(1)