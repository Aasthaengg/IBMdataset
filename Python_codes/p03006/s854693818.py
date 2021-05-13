from collections import Counter
from itertools import permutations
n=int(input())
if n==1:print(1);exit()
XY=[list(map(int,input().split())) for _ in range(n)]
A=[(X[0]-Y[0],X[1]-Y[1]) for X,Y in permutations(XY,2)]
print(n-max(Counter(A).values()))