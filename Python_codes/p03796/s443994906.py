n = int(input())

ans =1
for i in range(2,n+1):
    ans*=i
    ans = ans%int(1e9+7)

print(ans)