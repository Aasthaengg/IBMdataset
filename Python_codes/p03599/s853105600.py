A,B,C,D,E,F = map(int, input().split())

x = []
for i in range(0,F+1,A*100):
    for j in range(0,F+1,B*100):
        water = i + j
        if water > F:
            break
        x.append(water)

y = []
for i in range(0,F+1,C):
    for j in range(0,F+1,D):
        sugar = i + j
        if sugar > F:
            break
        y.append(sugar)

x = sorted(set(x))[1::]
y = sorted(set(y))

n = 0
WS = S = 0
for w in x:
    for s in y:
        if w + s > F:
            break
        if w * E//100 >= s:
            m = 100 * s / (w + s)
            if m >= n:
                n = m
                WS, S = w + s , s

print(WS,S)