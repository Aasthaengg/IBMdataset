N,T=map(int,input().split())
a=list(input().split())
ts=[]
for _ in range (len(a)):
    ts.append(int(a[_]))

YU=T

for i in range(1,N):
    if ts[i]-ts[i-1]<T:
        YU+=T-(T-(ts[i]-ts[i-1]))
    else:
        YU+=T
print (YU)