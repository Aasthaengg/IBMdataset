   #B=FLIP
n,m,k=map(int,input().split())
flag=False
for i in range(n+1):
    for j in range(m+1):
        if m*i+n*j-2*i*j==k:
            flag=True
            break
if flag:
    print("Yes")
else:
    print("No")