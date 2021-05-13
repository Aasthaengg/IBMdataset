x ,k ,d = map(int,input().split())

x = abs(x)
c = x // d
# 必要な移動回数
k_r = k - c
# 移動した後の残りの移動回数
ans_2 = x - d * c
#残り移動回数が偶数のときのｘからの距離

if c >= k:
    print(x - k * d )
    exit()

x_l = x - d * c
#ｘまでの残りの距離

if k_r % 2 == 0:
    print(ans_2)
    exit()
else :
    x_l -= d
    x_l =abs(x_l)
    print(x_l)