from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

iter = list(permutations(range(1, N+1), N))

for i in range(len(iter)):
    if iter[i] == P:
        p = i + 1
    if iter[i] == Q:
        q = i + 1
print(abs(p - q))
