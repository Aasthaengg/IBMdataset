import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = inintl()

odd = 0

for a in A:
    if a % 2 == 1:
        odd += 1

print("YES") if odd % 2 == 0 else print("NO")
