N,M=map(int,input().split())
X,Y=(list(map(int,input().split())) for i in range(2))
x1,x2=([0]*N for i in range(2))
y1,y2=([0]*M for i in range(2))
m=10**9+7
for i in range(N-1):
    x1[i+1]=(x1[i]+(X[i+1]-X[i])*(i+1))%m
    x2[i+1]=(x2[i]+x1[i])%m
for i in range(M-1):
    y1[i+1]=(y1[i]+(Y[i+1]-Y[i])*(i+1))%m
    y2[i+1]=(y2[i]+y1[i])%m
print(((x1[-1]+x2[-1])*(y1[-1]+y2[-1]))%m)