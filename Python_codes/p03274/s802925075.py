n, k = map(int, input().split())
X = list(map(int, input().split()))
ans = pow(10,9)+7
for i in range(n-k+1):
    ans = min(ans, min(abs(X[i])+abs(X[i+k-1]-X[i]), abs(X[i+k-1])+abs(X[i]-X[i+k-1])))
print(ans)