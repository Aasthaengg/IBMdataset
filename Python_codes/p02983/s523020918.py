L,R = list(map(int,input().split()))
if R-L+1 >= 2019:
    ans = 0
else:
    ans = 2019
    lis = [i%2019 for i in range(L,R+1)]
    for i in range(R-L):
        for j in range(i+1,R-L+1):
            s = (lis[i]*lis[j])%2019
            ans = min(s,ans)
print(ans)
