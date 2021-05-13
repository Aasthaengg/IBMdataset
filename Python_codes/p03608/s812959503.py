import itertools
def warshall_floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
d = [[float('inf') if i != j else 0 for j in range(N+1)]for i in range(N+1)]
# print(d)
for m in range(M):
    A, B, C = map(int, input().split())
    d[A][B] = C
    d[B][A] = C
warshall_floyd()
ans = float('inf')
for p in itertools.permutations(r):
    tmp = 0
    for i in range(len(p)-1):
        tmp += d[p[i]][p[i+1]]
    ans = min(tmp, ans)
print(ans)