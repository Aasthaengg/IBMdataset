N, K = map(int, input().split())  # N個の整数, 整数K
A = list(map(int, input().split()))
K += 1
k_bit = format(K, "b")
# 特定の桁に関して、どちらを立てたほうが調べておく
tmp = ""  # 下位桁の情報からappendしていき、最後にreverseを行う
for i in reversed(range(len(k_bit))):  # reversedして上位の桁から見ている
    bit = 1 << i
    count = 0  # i桁目について、ビットが立っている数の個数
    for a in A:
        if a & bit:
            count += 1
    if count > N - count:
        tmp += "0"
    else:
        tmp += "1"
# tmpには最適な答えが入っている
ans = 0  # 最終的な答え
for i in range(len(k_bit)):  # iが対象の桁, 上位から見ている
    if k_bit[i] == "0":
        continue
    x = k_bit[:i] + "0" + tmp[i+1:]
    num = int(x, 2)
    # もとまったnumについてループを回す
    hoge = 0
    for a in A:
        hoge += a ^ num
    ans = max(ans, hoge)
print(ans)
