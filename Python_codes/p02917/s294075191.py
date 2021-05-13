import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
B = inintl()

A = [B[0]]

for i in range(1,n-1):
    A.append(min(B[i], B[i-1]))

A.append(B[-1])

print(sum(A))
