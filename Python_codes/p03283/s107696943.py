import sys
input = sys.stdin.readline

N, M, Q = [int(x) for x in input().split()]
L = [0] * M
R = [0] * M
p = [0] * Q
q = [0] * Q
for i in range(M):
    L[i], R[i] = [int(x) for x in input().split()]
for j in range(Q):
    p[j], q[j] = [int(x) for x in input().split()]

train = [[0 for i in range(N + 1)] for _ in range(N + 2)]

for i in range(M): # すべての列車について
    train[L[i]][R[i]] += 1

for col in range(1, N + 1):
    for row in range(col, 0, -1):
        train[row][col] += train[row][col - 1] + train[row + 1][col] - train[row + 1][col - 1]

for j in range(Q):
    print(train[p[j]][q[j]])
