import sys
import math
from collections import Counter


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = input()

S = Counter(s)
a = S["a"]
b = S["b"]
c = S["c"]

if abs(a-b) <= 1 and abs(a-c) <= 1 and abs(c-b) <= 1:
    print("YES")
else:
    print("NO")