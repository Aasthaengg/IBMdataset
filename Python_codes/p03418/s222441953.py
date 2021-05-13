n,k = map(int,input().split())

ans = 0

for a in range(1,n + 1):
    ans+=max(a - k,0) * (n // a) + max(n % a - k + 1,0)

print(ans if k!=0 else n**2)