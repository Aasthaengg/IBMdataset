n,k = map(int,input().split())
X = list(map(int,input().split()))

ans = float('inf')
for i in range(n-k+1):
    x = X[i]
    y = X[i+k-1]
    if x==0 and y==0:
        ans = 0
    if x<0 and y<=0:
        ans = min(ans,abs(x))
    if x>=0 and y>0:
        ans = min(ans,y)
    if x<0 and y>0:
        ans = min(ans,min(abs(x),y)*2+max(abs(x),y))
    if X[i]>=0:
        break
print(ans)