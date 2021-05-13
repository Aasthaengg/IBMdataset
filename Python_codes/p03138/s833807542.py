N, K = map(int, input().split())
A = list(map(int, input().split()))

# 最大値を取るf(x)のxを求める
# digitsは下位桁 < 上位桁で1になっているbitをカウントする
digits = [0] * 40
for i in range(40):
    for a in A:
        if (a >> i) & 1:
            digits[i] += 1

# Kを考慮してmax_xを求める方法がわからない
# 桁ごとに最適なbitはすでにわかっていて、他の桁のbitに影響を受けることはないので、
# 上位桁から見ていって、Kが1になっている部分ならフラグを立てる
# 上位桁から見てKが1のbitが出てから、K:1,max_x:0のフラグを立てたら、その桁より下位桁のbitはなんでもよくなる
check_K = True
max_x = 0
for i, d in enumerate(reversed(digits)):
    i = 40 - i - 1
    if check_K and K < pow(2, i):
        continue
    if d <= (N-d) and ((K >> i) & 1 == 1 or not check_K):
        max_x += 2 ** i
    elif (K >> i) & 1 == 1:
        check_K = False
    
#print(max_x)
ans = 0
for a in A:
    ans += a ^ max_x

print(ans)

