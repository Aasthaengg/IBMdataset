n,m,k = map(int, input().split())
flag=0
for i in range(n+1):
    for j in range(m+1):
        if n*j+m*i-2*i*j==k:
            print("Yes")
            flag=1
            break
    if flag:
        break
if not flag:
    print("No")