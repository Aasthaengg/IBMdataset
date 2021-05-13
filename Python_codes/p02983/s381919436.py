L, R = map(int, input().split())

ans = 2019
for i in range(L, min(R+1, L+2020)):
    for j in range(i+1, min(R+1, L+2020)):
        ans = min(ans, ((i%2019)*(j%2019))%2019)
print(ans)