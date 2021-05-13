import sys
import re


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s=input()

if re.fullmatch("A?KIHA?BA?RA?", s):
    print("YES")
else:
    print("NO")
