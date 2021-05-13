
n,k = map(int,input().split())

if k == 0:
    print(n ** 2)
    exit()

ans = 0
for b in range(k+1,n+1):
    ans += (b - k)*(n//b)
    if n % b >= k > 0:
        ans += n%b - k + 1
    elif n%b >= k:
        ans = n%b - k
print(ans)
