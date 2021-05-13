# ２人で同じ個数になるように分ける。
# ３つの袋が同じ数かつ偶数の場合も分けれる。

a_box, b_box, c_box = map(int, input().split())

if a_box == b_box + c_box:
    print('Yes')
elif b_box == a_box + c_box:
    print('Yes')
elif c_box == a_box + b_box:
    print('Yes')
elif a_box == b_box == c_box and (a_box + b_box + c_box) % 2 == 0:
    print('Yes')
else:
    print('No')