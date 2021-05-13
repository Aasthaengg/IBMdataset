import itertools
import math

N=int(input())
X=[]
Y=[]
s=0
l=[int(x) for x in range(N)]
L = list(itertools.permutations(l, N))
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
for i in range(math.factorial(N)):
    for j in range(N-1):
        s+=((X[L[i][j]]-X[L[i][j+1]])**2+(Y[L[i][j]]-Y[L[i][j+1]])**2)**0.5
print(s/(math.factorial(N)))