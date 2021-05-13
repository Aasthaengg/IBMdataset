n,k = map(int,input().split())
X = list(map(int,input().split()))
ans = float("inf")
for i in range(n-k+1):
    ans = min(ans,abs(X[i])+abs(X[i]-X[i+k-1]),abs(X[i+k-1])+abs(X[i]-X[i+k-1]))
print(ans)