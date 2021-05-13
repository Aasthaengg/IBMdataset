N,T=map(int, input().split())
t=list(map(int,input().split()))
a=T
for i in range(1,N):
    if t[i]-t[i-1]>T:
        a+=T
    else:
        a+=t[i]-t[i-1]
print(a)
