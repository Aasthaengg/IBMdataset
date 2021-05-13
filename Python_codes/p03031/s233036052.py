from itertools import *
N,M = map(int,input().split())
K = [list(map(int,input().split()))[1:] for m in range(M)]
P = list(map(int,input().split()))
print(sum([all([sum([s[j-1] for j in v])%2==t for v,t in zip(K,P)]) for s in product([0,1],repeat=N)]))