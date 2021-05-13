import itertools
n = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
L = list(itertools.permutations([i for i in range(1,n+1)]))
print(
    abs((L.index(P)+1)-((L.index(Q)+1)))
    )
