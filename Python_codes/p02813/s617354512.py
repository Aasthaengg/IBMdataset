import itertools
N=int(input())
a=tuple(map(int,input().split()))
b=tuple(map(int,input().split()))
K=list(itertools.permutations(range(1,N+1)))
print(abs(K.index(a)-K.index(b)))