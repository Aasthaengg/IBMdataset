import itertools
N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))

A=list(itertools.permutations(list(range(1,N+1))))
print(abs(A.index(tuple(P))-A.index(tuple(Q))))