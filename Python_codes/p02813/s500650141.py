from itertools import permutations as per
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
PQ = list(per(list(range(1, N + 1))))

a = PQ.index(P) + 1
b = PQ.index(Q) + 1

print(abs(a - b))