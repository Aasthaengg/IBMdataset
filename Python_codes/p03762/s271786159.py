p=10**9+7

n,m=map(int,input().split())
x=list(map(int,input().split()))
w=[((x[i+1]-x[i])*(1+i)*(n-i-1))%p for i in range(n-1)]
y=list(map(int,input().split()))
h=[((y[k+1]-y[k])*(1+k)*(m-k-1))%p for k in range(m-1)]

print(((sum(w)%p)*(sum(h)%p)%p))