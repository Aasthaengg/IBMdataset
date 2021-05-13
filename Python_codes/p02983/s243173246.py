L, R = map(int, input().split())
P = R - L
if P >= 2019:
    print(0)
else:
    ans = 2019
    L %= 2019
    R = L + P
    for i in range(L, R):
        for j in range(i+1, R+1):
            ans = min(ans, (i*j)%2019)
    print(ans)