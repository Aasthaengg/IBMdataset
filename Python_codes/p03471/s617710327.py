n,y=map(int,input().split())

flag=0
total = 0

for i in range(n+1):
    for j in range(n+1):
        k=n-i-j
        if k<0:
            break

        total=10000*i+5000*j+1000*k
        if total==y:
            print(i,j,k)
            flag=1
            break 
    if flag == 1:
        break
if flag == 0:
    print('-1 -1 -1')