import sys
import math
from collections import Counter


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
D = inintl()
m = inint()
T = inintl()

D = Counter(D)

for t in T:
    D[t] -= 1

for i in D:
    if D[i] < 0:
        print("NO")
        exit()

print("YES")