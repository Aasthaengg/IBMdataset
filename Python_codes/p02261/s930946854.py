N, C = int(input()), [temp for temp in input().split()]
D    = list(C)

for i in range(N) :
    for j in range(i + 1, N)[ : : -1] :
        if int(C[j][1 :]) < int(C[j - 1][1 :]) :
            C[j], C[j - 1] = C[j - 1], C[j]
print(*C)
print('Stable')

for i in range(N) :
    minj = i
    for j in range(i, N) :
        if int(D[j][1 :]) < int(D[minj][1 :]) :
            minj = j
    D[i], D[minj] = D[minj], D[i]
print(*D)

cou = 0
for che in range(N) :
    if C[che] != D[che] :
        cou = 1
if cou == 0 : print('Stable')
else        : print('Not stable')