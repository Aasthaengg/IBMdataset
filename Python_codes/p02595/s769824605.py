X = list()
Y = list()
D = list()
score = 0

n,d = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(n):
    dis = (X[i]**2 + Y[i]**2)**0.5
    D.append(dis)

for i in range(n):
    if d >= D[i]:
        score += 1

print(score)