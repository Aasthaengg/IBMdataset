import math
x = int(input())

# 最大以上のどの点にも移動できる。
# max(i) = i*(i+1)/2

tar = (-1 + (1 + 8 * x) ** 0.5) * 0.5
ans = math.ceil(tar)

print(ans)