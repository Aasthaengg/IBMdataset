n,m = map(int,input().split())
*X, = map(int,input().split())
*Y, = map(int,input().split())
mod = 10**9+7

x,y=[],[]
for i,u in enumerate(X[:-1]):
    x.append(X[i+1]-u)
for i,v in enumerate(Y[:-1]):
    y.append(Y[i+1]-v)
wx = [(i+1)*(n-i-1)%mod for i in range(n-1)]
wy = [(i+1)*(m-i-1)%mod for i in range(m-1)]
print((sum([wx[i]*x[i] for i in range(n-1)])%mod)*(sum([wy[i]*y[i] for i in range(m-1)])%mod)%mod)