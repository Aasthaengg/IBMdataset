L, R = map(int, input().split())
# R-L>=2019なら、[L,R]に2019の倍数が必ず存在する
if R - L >= 2019:
    print(0)
else:
    ans = 10**9
    for i in range(L, R + 1):  # L<=i<=R
        for j in range(i + 1, R + 1):  # i<j<=R
            ans = min(ans, (i * j) % 2019)
    print(ans)
