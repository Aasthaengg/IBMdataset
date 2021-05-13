a, b, x = map(int, input().split())

# 0以上b以下で、xで割り切れる数の個数
temp1 = b // x + 1

# 0以上a-1以下で、xで割り切れる数の個数
# a==0の時だけ例外処理
if a == 0:
    temp2 = 0
else:
    temp2 = (a - 1) // x + 1

print(temp1 - temp2)
