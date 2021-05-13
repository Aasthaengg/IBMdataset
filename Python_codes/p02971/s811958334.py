import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = []
for _ in range(n):
    A.append(inint())

sorted_A = sorted(A)[::-1]

for a in A:
    if a != sorted_A[0]:
        print(sorted_A[0])
    else:
        print(sorted_A[1])
