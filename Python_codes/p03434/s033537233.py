import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = inintl()

alice = 0
bob = 0
A.sort()

for i in range(n):
    if i % 2 == 0:
        alice += A[i]
    else:
        bob += A[i]

print(abs(alice - bob))