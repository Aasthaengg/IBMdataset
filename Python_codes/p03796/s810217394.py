n = int(input())
m = 10**9+7

ans = 1
for i in range(2,n+1):
    ans = ans*i%m
print(ans%m)


