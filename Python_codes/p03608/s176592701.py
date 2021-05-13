from itertools import permutations
import sys
input = sys.stdin.readline

N, M, _ = list(map(int, input().split()))
R = list(map(int, input().split()))

T = [[float("inf")] * N for _ in range(N)]

for _ in range(M):
    A, B, C = list(map(int, input().split()))
    A -= 1
    B -= 1
    T[A][B] = T[B][A] = min(C, T[A][B])
for i in range(N):
    T[i][i] = 0

# T[j][i]: cost from j to i, O(V^3)
# T[j][i] = 0 if j == i


def warshall_floyd(T, V):
    for k in range(V):
        for j in range(V):
            for i in range(V):
                T[j][i] = min(T[j][i], T[j][k] + T[k][i])


warshall_floyd(T, N)


ans = float("inf")

for v in permutations(R):
    tmp = 0
    for i in range(len(v)-1):
        tmp += T[v[i]-1][v[i+1]-1]
    ans = min(ans, tmp)

print(ans)
