# https://atcoder.jp/contests/agc024/tasks/agc024_b

N = int(input())
A = [int(input()) - 1 for _ in range(N)]
Q = [0] * N
for i in range(N):
    Q[A[i]] = i

ans = 0
res = 1
for i in range(1, N):
    if Q[i] > Q[i - 1]:
        # keepできる
        res += 1
    else:
        # 回数をカウント
        ans = max(ans, res)
        res = 1
ans = max(ans, res)
# 全体 - 動かさない
print(N - ans)