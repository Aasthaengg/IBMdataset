n = int(input())
ans = 0
m = 10**9+7
ans = pow(10,n,m)
ans-=pow(9,n,m)*2
ans+=pow(8,n,m)
ans%=m
print(ans)