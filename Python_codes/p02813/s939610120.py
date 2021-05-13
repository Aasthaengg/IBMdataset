from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
for i, t in enumerate(permutations(range(1, N+1))):
    if t == P:
        p = i
    if t == Q:
        q = i
print(abs(p-q))
