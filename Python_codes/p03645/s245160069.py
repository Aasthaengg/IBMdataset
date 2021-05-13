N_shima, M_fune = map(int, input().split())

shima_1 = []
shima_N = []

for i in range(M_fune):
    a, b = map(int, input().split())

    if (a == 1):
        shima_1.append(b)
    elif (a == N_shima):
        shima_N.append(b)
    if (b == 1):
        shima_1.append(a)
    elif (b == N_shima):
        shima_N.append(a)
    
judge = set(shima_1) & set(shima_N)

if (len(judge) >= 1):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
