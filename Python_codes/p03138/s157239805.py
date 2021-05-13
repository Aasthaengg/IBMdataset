"XXOR"
N, K = map(int, input().split())
A = list(map(int, input().split()))
# 2進数で41桁の理想的な数字を求める
K += 1
binary_K = format(K, '041b')
ideal_x = ""
for i in reversed(range(41)):
    bit = 1 << i
    count = 0
    # 大きい桁から、bitが立っている数をカウントする
    for a in A:
        if a & bit:
            count += 1
    if count > N - count:  # 1の方が多いなら
        ideal_x += "0"
    else:
        ideal_x += "1"
# print(binary_K)
# print(ideal_x)
# binary_Kより小さい範囲で理想的なxを探す
ans = 0
for i in range(41):
    if binary_K[i] == "0":
        continue
    x = binary_K[:i] + "0" + ideal_x[i+1:]
    x = int(x, 2)
    fx = 0
    for a in A:
        fx += a ^ x
    ans = max(ans, fx)
print(ans)
