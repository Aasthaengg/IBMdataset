a, b, c, d, e, f = map(int, input().split())

X, Y = [], []
for i in range(int(f / 100 + 0.9)):
    for j in range(int(f / 100 + 0.9)):
        x = 100 * a * i + 100 * b * j
        if x <= f:
            X.append(x)

for i in range(int(f / c + 0.9)):
    for j in range(int(f / d + 0.9)):
        y = c * i + d * j
        if y <= f:
            Y.append(y)

X = list(set(X))
Y = list(set(Y))

res = [0, 0]
p = e / (100 + e) # 最大濃度
maxP = 0 # ありうる最大濃度
for x in X:
    for y in Y:
        if x + y > 0 and x + y <= f: # 質量制約
            if y / (x + y) <= p: # 溶けるかどうか
                # res.append([x, y])
                if y / (x + y) >= maxP:
                    res[0] = x + y
                    res[1] = y
                    maxP = y / (x + y)
    
print(*res)
