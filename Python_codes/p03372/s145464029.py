from itertools import accumulate
N, C = map(int, input().split())
X, V = [], []
for i in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)


# 右回り・左回りに進んだ場合の、効用の累積和
R_acc_val = [0] + list(accumulate(V))
L_acc_val = [0] + list(accumulate(V[::-1]))


# 右回り・左回りに進んだ場合のコストを加味した効用
R_val, L_val = [0], [0]
for i in range(1, N + 1):
    R_val.append(R_acc_val[i] - X[i - 1])
    L_val.append(L_acc_val[i] - (C - X[-i]))


# コストを加味した効用の、max累積和
R_max_val, L_max_val = list(accumulate(R_val, func=max)), list(accumulate(L_val, func=max))


ans = 0
for i in range(N + 1):
    ans = max(ans,
              R_val[i],
              R_val[i] + L_max_val[-i-1] - X[i - 1],
              L_val[i],
              L_val[i] + R_max_val[-i-1] - (C - X[-i]))

print(ans)
