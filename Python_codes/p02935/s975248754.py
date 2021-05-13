import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
V = inintl()

V = sorted(V)

now = 0

for i in range(n-1):
    now = (V[i]+V[i+1])/2
    V[i+1] = now

print(now)