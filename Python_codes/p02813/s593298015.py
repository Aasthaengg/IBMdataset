from itertools import permutations

n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

L = list(permutations(range(1, n+1), n))
print(abs(L.index(P) - L.index(Q)))