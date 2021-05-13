N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
# 小さいAと大きいF, 大きいAと小さいFの組を作りたい
A.sort()
F.sort(reverse=True)

# 最大値の最小化 -> 二分探索
# 目標値Xを達成できるか？

# ありうる最小値-1
left = -1
# ありうる最大値+1
right = 10**12 + 1
while right - left > 1:
    mid = (left + right) // 2
    cnt = 0
    for i in range(N):
        # スコアをmidにするために必要な「修行の回数」
        # 負になった場合は0にする（修行は必要ない）
        tmp = max(A[i] - mid // F[i], 0)
        cnt += tmp
    if cnt <= K:
        right = mid
    else:
        left = mid

print(right)
