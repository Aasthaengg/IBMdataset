N,M,C = map(int, input().split())
B = list(map(int, input().split()))
cnt = 0

for _ in range(N):
    A = list(map(int, input().split()))
    s = C
    for j in range(M):
        s += A[j] * B[j]
    if s > 0:
        cnt += 1
print(cnt)