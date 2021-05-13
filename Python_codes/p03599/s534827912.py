A,B,C,D,E,F = map(int,input().split())
W = []
S = []

# 100A,100B の水
for a in range(1 + F // 100):
    for b in range(1 + F // 100):
        water = 100 * (a * A + b * B)
        if 0 < water <= F:
            W.append(water)

# c,d の砂糖
for c in range(1 + F // C):
    for d in range(1 + F // D):
        sugar = c * C + d * D
        if sugar <= F:
            S.append(sugar)

W = list(set(W))
S = list(set(S))

x = -1
for w in W:
    for s in S:
        if w + s <= F:
            sol = 100 * s / w
            if x < sol <= E:
                x = sol
                X, Y = w + s, s

print(X,Y)
