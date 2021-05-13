N, Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]

# 累積和
cumsum = [0] * (N + 1)
for i in range(N):
    if i + 1 < N and S[i] == "A" and S[i + 1] == "C":
        cumsum[i + 1] = cumsum[i] + 1
    else:
        cumsum[i + 1] = cumsum[i]

# クエリ
for q in LR:
    l = q[0] - 1
    r = q[1] - 1
    print(cumsum[r] - cumsum[l])
