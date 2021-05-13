import itertools
N  = int(input())
P = tuple(map(int,input().split())) 
Q = tuple(map(int,input().split()))
List = list(itertools.permutations(range(1,N+1)))
ans = abs(List.index(Q) - List.index(P))
print(ans)