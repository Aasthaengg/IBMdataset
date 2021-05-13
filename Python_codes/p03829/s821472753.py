N,A,B = map(int,input().split())
X = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    x = X[i]
    y = X[i+1]
    a = (y-x)*A
    if a <= B:
        ans += a
    else:
        ans += B
print(ans)