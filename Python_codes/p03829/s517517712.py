N,A,B=map(int,input().split())
X=list(map(int,input().split()))
ans = 0
x = X[0]
for i in range(N):
    ans += min((X[i]-x)*A, B)
    x = X[i]
print(ans)