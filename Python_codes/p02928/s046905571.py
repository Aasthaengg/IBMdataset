INF = 10 ** 9 + 7

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 単体のA内で発生するケース
inv = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            inv += 1
inv = inv * K

# 異なるA間で発生するケース
ini = 0
for k in range(N):
    for l in range(N):
        if A[k] > A[l]:
            ini += 1
ini = ini * K * (K-1) // 2
ans = (inv+ini) % INF
print(ans)
