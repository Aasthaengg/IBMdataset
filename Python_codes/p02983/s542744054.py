L,R = list(map(int,input().split()))
if R-L+1 >= 2019:
    ans = 0
else:
    ans = 2019
    for i in range(L,R):
        for j in range(i+1,R+1):
            s = (i*j)%2019
            ans = min(s,ans)
print(ans)
