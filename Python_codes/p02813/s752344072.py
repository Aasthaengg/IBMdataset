import itertools
N=int(input())
l=list(itertools.permutations([i for i in range(1,N+1)],N))
val1=tuple(map(int,input().split()))
val2=tuple(map(int,input().split()))
print(abs(l.index(val1)-l.index(val2)))