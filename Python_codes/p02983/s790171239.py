L,R = list(map(int,input().split()))

ans = 10**9
if R-L >= 2020:
    for i in range(L,L+2019):
        for j in range(L+1,L+2020):
            ans = min(ans,(i*j)%2019)
else:
    for i in range(L,R):
        for j in range(L+1,R+1):
            ans = min(ans,(i*j)%2019)

print(ans)