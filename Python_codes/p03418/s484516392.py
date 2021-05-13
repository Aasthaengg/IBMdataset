n,k = map(int,input().split())

ans = 0

for i in range(k+1,n+1):
    kosu = n // i
    ans += kosu*(i-(k+1)+1)
    if n % i == 0:
        continue
    if k == 0:
        ans += max(0,n%i-k)
    else:
        ans += max(0,n%i-(k-1))
   # print(i,ans)
    
print(ans)