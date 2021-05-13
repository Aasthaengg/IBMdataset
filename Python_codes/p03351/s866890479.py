# 097a

a, b, c, d = map(int, input().split())  # a,b,c,dを代入

if (a - b) >= 0:
    ab = a - b  # aとbの距離abを代入
else:
    ab = (a - b) * -1   # 距離が負の場合は-1を掛けて正の値にする

if (a - c) >= 0:
    ac = a - c
else:
    ac = (a - c) * -1

if (b - c) >= 0:
    bc = b - c
else:
    bc = (b - c) * -1

if ac <= d:
    print('Yes')
elif ab <= d and bc <= d:
    print('Yes')
else:
    print('No')
