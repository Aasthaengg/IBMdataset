n,m=map(int,input().split())
if(m%2==1):
    print("No")
elif(2*n<=m and m<=4*n):
    print("Yes")
else:
    print("No")
