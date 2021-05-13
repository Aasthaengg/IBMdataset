def inpl(): return list(map(int, input().split()))
A, B, M = inpl()
A = inpl()
B = inpl()
res = min(A) + min(B)
for _ in range(M):
    x, y, c = inpl()
    tmp = A[x-1] + B[y-1] - c
    if tmp < res:
        res = tmp
print(res)