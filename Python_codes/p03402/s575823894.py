a, b = map(int, input().split())
a -= 1
b -= 1

# 上半分は'#'，下半分は'.'
B = [['#'] * 100 if i < 50 else ['.'] * 100 for i in range(100)]

# 上から49行目までを，上下左右斜めで隣接しないように'#'を'.'に塗り替える
for h in range(0, 49, 2):
    tmp = 0
    while a != 0 and tmp < 100:
        B[h][tmp] = '.'
        a -= 1
        tmp += 2

# 下から49行目までを，上下左右斜めで隣接しないように'.'を'#'に塗り替える
for h in range(51, 100, 2)[::-1]:
    tmp = 0
    while b != 0 and tmp < 100:
        B[h][tmp] = '#'
        b -= 1
        tmp += 2

print(100, 100)
for b in B:
    print(*b, sep='')