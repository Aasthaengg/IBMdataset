N = int(input())
X = list(map(int, input().split()))

X_g = sum(X)/N

if X_g%1<0.5:
    P = int(X_g)
else:
    P = int(X_g)+1
ans = 0
for i in range(N):
    ans += (X[i]-P)**2

print(ans)
