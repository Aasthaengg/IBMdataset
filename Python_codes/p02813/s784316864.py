import itertools

N = int(input())
P = tuple((int(i) for i in input().split()))
Q = tuple((int(i) for i in input().split()))

f = list(itertools.permutations(range(1, N+1)))

print(abs(f.index(P) - f.index(Q)))