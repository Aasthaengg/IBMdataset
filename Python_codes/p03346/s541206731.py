N=int(input())
P=[int(input()) for _ in range(N)]

def solve():
    O=[-1]*(N+1)
    for i,p in enumerate(P): O[p]=i

    n=0
    nn=0
    for i in range(1,N+1):
        if O[i-1]<O[i]: n+=1
        else: n=1
        nn=max(nn,n)

    return N-nn

print(solve())
'''
from itertools import permutations
for p in permutations(range(N)):
    P=list(map(lambda x:x+1,p))
    print(P,solve())
'''