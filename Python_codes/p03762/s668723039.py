n,m,=map(int,input().split())
*x,=map(int,input().split())
*y,=map(int,input().split())
mod=10**9+7
print(sum((2*i-n-1)*x[i-1]for i in range(1,n+1))*sum((2*i-m-1)*y[i-1]for i in range(1,m+1))%mod)