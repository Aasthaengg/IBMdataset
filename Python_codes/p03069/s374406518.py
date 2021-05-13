N = int(input())
S = input()
sum_b = [0]
sum_w = [0]
b = 0
w = 0

for s in S:
    if s == "#":
        b += 1
    else:
        w += 1
    # 白黒の累積和作る
    sum_b.append(b)
    sum_w.append(w)

ans = float("inf")
for i in range(N + 1):
    # i番目までにある黒をすべて白にし、それ以降の白をすべて黒にするのに必要な手数
    buf = sum_b[i] + (sum_w[-1] - sum_w[i])
    # 更新するか否か
    ans = min(ans, buf)

print(ans)