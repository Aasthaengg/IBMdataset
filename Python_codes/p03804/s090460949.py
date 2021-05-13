n,m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

flag = False  
for i in range(n-m+1):
    #flag = True
    for k in range(n-m+1):
        flag=True#ここ
        for j in range(i,i+m):
            #if i==k==3:
            #    print(a[j][k:k+m],b[j-i],a[j][k:k+m]==b[j-i],flag)
            if a[j][k:k+m]!=b[j-i]:
                flag = False
                break
        if flag:
            break
    if flag:
        break
#print(i,k,flag)        
print("Yes" if flag else "No")
