MOD=10**9+7
n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x_sum=sum((2*i-n+1)*x[i]for i in range(n))
y_sum=sum((2*i-m+1)*y[i]for i in range(m))
print(x_sum*y_sum%MOD)