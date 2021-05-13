N = int(input())
A = [0] + list(map(int, input().split()))

# 各山に降った雨の量
X = [0] * (N + 1)

# まずx[1]を求める
# X[1] + ... + X[N] = A[1] + ... + A[N]
# X[2]+X[3] = 2*A[2], X[4]+X[5] = 2*A[4], ...より、
# X[1] = A[1] - A[2] + A[3] - ... + A[N]

tmp = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        tmp += A[i]
    else:
        tmp -= A[i]
X[1] = tmp

# x[2],x[3],...,x[N]を漸化式から求める
for i in range(2, N + 1):
    X[i] = 2 * A[i - 1] - X[i - 1]
print(*X[1:])
