import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())

lst = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    L, R = map(int, input().split())
    for l in range(L + 1):
        lst[l][R] += 1

for l in range(N + 1):
    for r in range(N):
        lst[l][r + 1] += lst[l][r]

# for tmp in lst:
#     print (tmp)

for _ in range(Q):
    p, q = map(int, input().split())
    print (lst[p][q])