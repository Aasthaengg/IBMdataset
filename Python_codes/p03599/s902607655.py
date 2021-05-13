A, B, C, D, E, F = map(int, input().split())

ab_list = []
for a in range(F//100+1):
    for b in range(F//100+1):
        x = A*a + B*b
        if (0 < 100*x <= F) and (x not in ab_list):
            ab_list.append(x)

cd_list = []
for c in range(F+1):
    for d in range(F+1):
        y = C*c + D*d
        if (y <= F) and (y not in cd_list):
            cd_list.append(y)

max_conc = 0
result = [0, 0]
for i in ab_list:
    for j in cd_list:
        if (100*i + j <= F) and (j <= E*i):
            conc = (100*j) / (100*i + j)
            if conc >= max_conc:
                max_conc = conc
                result = [100*i + j, j]

print(result[0], result[1])