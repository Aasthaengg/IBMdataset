# Xi = 0, Ki = 1となる場所を探す旅に出る。
# K+=1して、Xi=0, Ki=1となる場所を作ればX =< Kの条件を満たすことができる。
N, K = map(int, input().split())
A = list(map(int, input().split()))
K += 1
K_bit = format(K, "b")
# iを探す
tmp = ""  # まず最適な数字を探す
for i in reversed(range(len(K_bit))):
    # 上からi桁目のビットが立っているか確認
    bit = 1 << i
    count = 0
    for a in A:
        if a & bit:
            count += 1
    if count > N - count:
        tmp += "0"
    else:
        tmp += "1"
# 最適なtmpができた
ans = 0
for i in range(len(K_bit)):
    bit = 1 << i
    if K_bit[i] == "1":  # i桁目が立っている時に初めてXi=0, Ki=1にできる
        num = K_bit[:i] + "0" + tmp[i+1:]
        num = int(num, 2)
        fx = 0
        for a in A:
            fx += num ^ a
        ans = max(ans, fx)
    else:
        continue
print(ans)
