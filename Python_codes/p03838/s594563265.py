import sys
x, y = map(int, input().split())

# aが正なら絶対値を増やすべき、そうでなければ減らすべき
a = abs(y) - abs(x)

# 符号が違うだけなら符号反転して終わり
if a == 0 and x != y:
    print(1)
    sys.exit()

# 最初に符号反転するべきか
push = 0
if (a < 0 and x > 0) or (a > 0 and x < 0):
    push += 1
    x = -x

# 加算
x += abs(a)

# 最後に符号反転するべきか
if x != y:
    push += 1

print(abs(a) + push)