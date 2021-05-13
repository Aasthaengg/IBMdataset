# Atcoder Review Problems
# sugar Water
A, B, C, D, E, F = map(int, input().split())
# 別々に構成してもいい
dp_sugar = [0 for i in range(3001)]
dp_sugar[0] = True
for i in range(1, 3001):
    if i >= C:
        dp_sugar[i] |= dp_sugar[i-C]
    if i >= D:
        dp_sugar[i] |= dp_sugar[i-D]

dp_water = [0 for i in range(3001)]
dp_water[0] = 1
for i in range(1, 3001):
    if i >= 100*A:
        dp_water[i] |= dp_water[i-100*A]
    if i >= 100*B:
        dp_water[i] |= dp_water[i-100*B]

data = []
for i in range(1, F+1):
    # 水の量をiで固定
    if dp_water[i]:
        submax = 0
        for j in range(F+1-i):
            # 砂糖の量j
            if dp_sugar[j] and 100*j <= E*i:
                submax = j
        data.append((i+submax, submax, 100*submax/(i+submax)))
data.sort(key=lambda x: x[-1])
x,y,z=data[-1]
print(x,y)