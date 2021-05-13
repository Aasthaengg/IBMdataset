K, A, B = map(int, input().split())

ans = 1
if A >= B:
    ans += K
else:
    restk = K
    # A < B
    restk -= A - 1

    if restk <= 0:
        ans += K
    else:
        if restk > 1:
            ans = max(K+1, A + (restk // 2)*(B - A) + restk % 2)
        else:
            ans = A + 1
print(ans)
