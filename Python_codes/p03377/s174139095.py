import math
import itertools
#n = int(input())
#n, d = list(input().split())
A, B, X= list(map(int, input().split()))

if A == X or (A < X and A+B > X) :
    print("YES")
else:
    print("NO")