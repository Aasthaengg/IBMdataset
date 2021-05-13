X, K, D = map(int, input().split())

ans = 0
if abs(X) >= K*D:
    ans = abs(X) - K*D
else:
    if (K - abs(X)//D)%2 == 0:
        ans = abs(X)%D
    else:
        ans = D - abs(X)%D

print(ans)