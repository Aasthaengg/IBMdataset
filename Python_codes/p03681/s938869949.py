n,m=map(int,input().split())
if n==m:
    temp=1
    for i in range(1,n+1):
      temp=(temp*i)%(10**9+7)
    print((2*((temp*temp)%(10**9+7)))%(10**9+7))
elif abs(n-m)==1:
    temp1=1
    temp2=1
    for i in range(1,n+1):
        temp1=(temp1*(i%(10**9+7)))%(10**9+7)
    for j in range(1,m+1):
        temp2=(temp2*(j%(10**9+7)))%(10**9+7)
    print((temp1*temp2)%(10**9+7))
else:
    print(0)