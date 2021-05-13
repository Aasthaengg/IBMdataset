import sys
input = sys.stdin.readline
N, M, Q = map(int, input().split())

sum_table = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    l, r = map(int, input().split())
    sum_table[l][r] += 1

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_table[i][j] += sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1]

for _ in range(Q):
    p, q = map(int, input().split())
    print(sum_table[q][q] - sum_table[q][p-1] - sum_table[p-1][q] + sum_table[p-1][p-1])


