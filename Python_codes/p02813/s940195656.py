import itertools
N = int(input())
lis = list(itertools.permutations(range(1, N+1)))
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
P = tuple(P)
Q = tuple(Q)
a = lis.index(P) + 1
b = lis.index(Q) + 1
ans = abs(a - b)
print(ans)