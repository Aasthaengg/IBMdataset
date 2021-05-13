import sys
input=sys.stdin.readline
INF=10**9+7
n,m=map(int,input().split())
x_list=list(map(int,input().split()))
y_list=list(map(int,input().split()))
X=0
plus=0
for i in range(n-1):
    plus=(plus+(x_list[i+1]-x_list[i])*(i+1))%INF
    X=(X+plus)%INF
Y=0
plus=0
for i in range(m-1):
    plus=(plus+(y_list[i+1]-y_list[i])*(i+1))%INF
    Y=(Y+plus)%INF
ans=(X*Y)%INF
print(ans)
    
    
