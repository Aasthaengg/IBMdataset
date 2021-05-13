import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n,k,q = inintm()
A = []
con = [0]*n

border = q-k

for _ in range(q):
    A.append(inint())

for a in A:
    con[a-1] += 1

for c in con:
    if c > border:
        print("Yes")
    else:
        print("No")

