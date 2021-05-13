n,y = map(int,input().split())
flag = 0
y_10 = 0
y_5 = 0

for i in range(n+1):
    y_10 = i * 10000
    if y_10 > y:
        break
    for j in range(0,n-i+1):
        y_5 = j*5000
        if y_10+y_5 > y:
            break
        k = n-i-j
        if y_10 + y_5 + 1000*k == y:
            print(i,j,k)
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print('-1 -1 -1')
