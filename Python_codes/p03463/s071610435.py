import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, a, b = inintm()

if n == 2:
    print("Borys")
    exit()

print("Alice") if (abs(a-b)-1) % 2 == 1 else print("Borys")
