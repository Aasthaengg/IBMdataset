k, s = map(int,input().split())
# print(k)
# print(s)

# 組み合わせをカウントする変数
count = 0

# 変数の初期化
x = 0
y = 0
z = 0

for x in range(k+1):
    for y in range(k+1):
        z = s - x - y
        if z >= 0 and z <= k:
            count += 1

print(count)
