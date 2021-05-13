import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
T = inintl()
m = inint()

for i in range(m):
    p, x = inintm()
    t = T[p-1]
    T[p-1] = x
    print(sum(T))
    T[p-1] = t