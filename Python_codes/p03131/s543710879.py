import sys


INF = 10**60
inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

k, a, b = inintm()
ans = 0

if a + 2 >= b:
    print(1+k)
else:
    ch = max(0, (k-(a-1))//2)
    print(b + (ch-1)*(b-a) + k-(ch*2+a-1))
