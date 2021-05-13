mod=10**9+7
n,m=map(int,input().split())
X=tuple(map(int,input().split()))
Y=tuple(map(int,input().split()))
ans_x,ans_y=0,0
for i,x in enumerate(X):
    ans_x+=(2*i+1-n)*x
    ans_x%=mod
for i,y in enumerate(Y):
    ans_y+=(2*i+1-m)*y
    ans_y%=mod
print((ans_x*ans_y)%mod)