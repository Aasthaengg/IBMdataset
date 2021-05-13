n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
Z = []
Z_x = []
f_y = False
for i in range(X+1, Y+1):
    Z.append(i)  #X < Z <= Yをappend

###Zの範囲で条件を満たすZのみZ_xにappend
for i in range(len(Z)):
    cnt_x = 0
    for j in range(len(x)):
        if Z[i] > x[j]:
            cnt_x += 1
    if cnt_x == len(x):
        Z_x.append(Z[i])

###条件を満たし、新たにできたZの範囲で条件を満たすYを探す
for i in range(len(Z_x)):
    cnt_y = 0
    for j in range(len(y)):
        if Z_x[i] <= y[j]:
            cnt_y += 1
    if cnt_y == len(y):
        f_y = True
        break

if f_y:
    print('No War')
else:
    print('War')