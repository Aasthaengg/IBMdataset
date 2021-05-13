N, Q = map(int, input().split())
S = input()
lr = [list(map(int, input().split())) for _ in range(Q)]

# 累積和
cumSum = [0] * (N + 1)

cnt = 0

for i in range(1, N):
    pre = S[i - 1]
    now = S[i]

    if pre == "A" and now == "C":
        cnt += 1

    cumSum[i + 1] = cnt
    pre = now

for l, r in lr:
    print(cumSum[r] - cumSum[l])
