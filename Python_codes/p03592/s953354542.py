n,m,k = map(int,input().split())
flag = False
for i in range(n+1):
    for j in range(m+1):
        if (n-2*i)*(m-2*j) == n*m-2*k:
            print("Yes")
            flag = True
            break
    if flag == True:
        break
if flag == False:
    print("No")