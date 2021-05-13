from itertools import permutations
N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
P=tuple(map(lambda x: x-1,P))
Q=tuple(map(lambda x: x-1,Q))
l=list(permutations(range(N)))
print(abs(l.index(P)-l.index(Q)))