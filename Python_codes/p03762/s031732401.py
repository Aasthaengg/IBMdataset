n,m=map(int,input().split())
*x,=map(int,input().split())
*y,=map(int,input().split())
mod=10**9+7

w,h=0,0
for i in range(n):
    w+=(2*i+1-n)*x[i]
for i in range(m):
    h+=(2*i+1-m)*y[i]
print(w*h%mod)