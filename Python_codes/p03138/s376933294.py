N, K = map(int, input().split())
A = list(map(int, input().split()))
# dp[上からi桁まで][smaller]
dp = [[-1 for _ in range(2)]for _ in range(51)]
dp[0][0] = 0
MAX_DIGIT = 50

for d in range(MAX_DIGIT):
    # d = 0なら1<<49
    # d = 49なら1<<0
    mask = 1 << (MAX_DIGIT - d - 1)

    # A で元々 d 桁目にビットが立っているものの個数
    num = 0
    for i in range(N):
        if A[i] & mask:
            num += 1
    # X の d 桁目を 0, 1 にしたときのスコア
    cost0 = mask * num
    cost1 = mask * (N - num)

    # smaller -> smaller
    # 0 でも 1 でも良い、スコアが大きい方
    if dp[d][1] != -1:
        dp[d + 1][1] = max(dp[d + 1][1], dp[d][1] + max(cost0, cost1))

    # exact -> smaller
    # K の d 桁目が 1 だったら、X の d 桁目は 0 にする
    if dp[d][0] != -1:
        if K & mask:
            dp[d + 1][1] = max(dp[d + 1][1], dp[d][0] + cost0)

    # exact -> exact (K にぴったり合わせる)
    if dp[d][0] != -1:
        if K & mask:
            dp[d + 1][0] = max(dp[d + 1][0], dp[d][0] + cost1)
        else:
            dp[d + 1][0] = max(dp[d + 1][0], dp[d][0] + cost0)

print(max(dp[MAX_DIGIT][0], dp[MAX_DIGIT][1]))
# print(dp)
