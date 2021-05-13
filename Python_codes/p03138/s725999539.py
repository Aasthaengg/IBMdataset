n, k = map(int, input().split())
A = list(map(int, input().split()))
one = [0] * 40
zero = [0] * 40
for i in range(40):
    for a in A:
        if a >> i & 1:
            one[i] += 1
        else:
            zero[i] += 1
dp1 = [-1e10] * 41 # 上から 40 - i 桁目までみたとき、 K と同じ
dp2 = [-1e10] * 41 # 上から 40 - i 桁目までみたとき、 K より小さい
dp1[40] = 0
for i in range(39, -1, -1):
    if k >> i & 1:
        dp2[i] = max(dp2[i + 1] * 2 + max(zero[i], one[i]), dp1[i + 1] * 2 + one[i])
        dp1[i] = dp1[i + 1] * 2 + zero[i]
    else:
        dp2[i] = dp2[i + 1] * 2 + max(zero[i], one[i])
        dp1[i] = dp1[i + 1] * 2 + one[i]
print(max(dp1[0], dp2[0]))