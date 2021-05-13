N = int(input())
S = list(input())
shiro_sum = [0] * (N+1)
kuro_sum = [0] * (N+1)
for i in range(N):
    if S[i] == '.':
        shiro_sum[i+1] = shiro_sum[i] + 1
    else:
        shiro_sum[i+1] = shiro_sum[i] + 0

    if S[i] == '#':
        kuro_sum[i+1] = kuro_sum[i] + 1
    else:
        kuro_sum[i+1] = kuro_sum[i] + 0

res = 10**9
# i == 0
for i in range(N+1):
    tmp = 0
    # leftを全て白に
    # 左側にある黒の数を数える。
    tmp += kuro_sum[i]

    # rightを全て黒に
    # 右側にある白を数えて、全体の数から白の合計を消す
    tmp += shiro_sum[N] - shiro_sum[i]
    res = min(res, tmp)
print(res)
