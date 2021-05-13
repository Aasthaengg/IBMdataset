n,m = (int(i) for i in input().split())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
difx,dify,num,num2,mod = [],[],0,0,10**9+7
for i in range(1,n): difx.append(x[i]-x[i-1])
for i in range(1,m): dify.append(y[i]-y[i-1])
for i in range(n-1): num = (num+(i+1)*(n-i-1)*difx[i])%mod
for i in range(m-1): num2 = (num2+(i+1)*(m-i-1)*dify[i])%mod
print(num*num2%mod)