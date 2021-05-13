L,R = list(map(int, input().split()))

ans = 10**12
for i in range(L, R+1):
    tmp = i - L+1
    for j in range(L+tmp, R+1):
        ans = min(ans, i*j % 2019)
        if(ans == 0):
            print(0)
            exit()

print(ans)