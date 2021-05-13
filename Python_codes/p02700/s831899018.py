# 高橋 HP:a ATK:b
# 青木 HP:c ATK:d
a, b, c, d = map(int, input().split())

# 高橋が主人公
while a >= 0 or c >= 0:
    a = a - d
    c = c - b
    if c <= 0:
        print('Yes')
        break
    elif a <= 0:
        print('No')
        break

