X, K, D = map(int, input().split())

ans = 0

if abs(X) > K*D:
    ans = abs(X) - K*D
else:
    k = abs(X)//D
    if (K-k)%2 == 0:
        ans = abs(X) - D*k
    else:
        ans = D - (abs(X) - D*k)

print(ans)