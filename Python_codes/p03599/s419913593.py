A, B, C, D, E, F = map(int, input().split())
x_list = []
y_list = []
noudo = []
for i in range(F):
    for j in range(F):
        if C*i + D*j <= F:
            y_list.append(C*i + D*j)

for i in range(F//100):
    for j in range(F//100):
        if A*i + B*j <= F//100:
            x_list.append(100 * (A*i + B*j))
x_list.remove(0)
for x in x_list:
    for y in y_list:
        if x+y <= F and y / (x+y) <= E / (100+E):
            noudo.append([y / (x+y), x+y, y])

ans = max(noudo)
print(ans[1], ans[2])