N = int(input())
print(0, flush=True)
s0 = input()
if s0 == 'Vacant':
    exit()
l = 0
r = N-1

while r - l > 1:
    m = (l+r) // 2  # 中央値のクエリを送る
    print(m, flush=True)
    s = input()
    if s == 'Vacant':
        exit()
    if m % 2 == 1:  # r-lが奇数であることと同義
        if s != s0:  # 異性ならば
            l = m  # 前半部分に空席はないから下限をあげる
        else:  # 同性ならば
            r = m  # 前半部分に空席があるので上限を下げる
    else:  # r-lが偶数であることと同義
        if s != s0:  # 異性ならば
            r = m  #
        else:  # 同性ならば
            l = m
print(r, flush=True)
sr = input()
