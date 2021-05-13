N, K = map(int, input().split())
P = list(map(int, input().split()))
A = [(p + 1) / 2 for p in P]
B = [0 for i in range(N)]
B[0] = A[0]
for i in range(1, N):
    B[i] = B[i - 1] + A[i]
ans = 0
for i in range(K - 1, N):
    if i == K - 1:
        a = B[i]
    else:
        a = B[i] - B[i - K]
    if ans < a:
        ans = a
print(ans)
