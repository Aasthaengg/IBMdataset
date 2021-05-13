N = int(input())
P = [int(input()) - 1 for i in range(N)]

A = [0] * N
for i, p in enumerate(P):
    A[p] = i

cnt, res = 1, 0
for i in range(N - 1):
    if A[i] < A[i + 1]:
        cnt += 1
    else:
        res = max(res, cnt)
        cnt = 1
res = max(res, cnt)
print(N - res)