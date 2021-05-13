N = int(input()) # ボールの数
K = int(input()) # Bの位置
xs = [int(i) for i in input().split()] # ボールの位置

half = K / 2

total = 0
for x in xs:
    if x < half:
        total += x
    else:
        total += (K-x)

# 最後に二倍すればよい
print(2*total)

