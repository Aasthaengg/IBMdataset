from itertools import accumulate
N, C = map(int, input().split())

X, V = [], []
for i in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)


# 右向き・左向きに進み、i番目の寿司までたどり着いた時点のコストを無視したエネルギー
R_v = list(accumulate(V))
L_v = list(accumulate(V[::-1]))

# 右向き・左向きに進み、i番目の寿司までたどり着いた時点のエネルギー
R_xv, L_xv = [], []
for i in range(N):
    R_xv.append(R_v[i] - X[i])
    L_xv.append(L_v[i] - (C - X[N - i - 1]))

# 右向き・左向きに進み、i番目の寿司までたどり着いた時点のエネルギーのmax累積和
R_xv_max = list(accumulate(R_xv, func=max))
L_xv_max = list(accumulate(L_xv, func=max))

ans = 0
for i in range(N):
    ans = max(ans, R_xv[i], L_xv[i])
    if i < N - 1:
        ans = max(ans,
                  R_xv[i] - X[i] + L_xv_max[N - i - 2],
                  L_xv[i] - (C - X[N - i - 1]) + R_xv_max[N - i - 2]
                  )

print(ans)
