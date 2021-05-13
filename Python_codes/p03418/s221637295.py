n,k=map(int,input().split())

ans = 0
for b in range(k+1,n+1):
    ans += max(n%b - (k-1),0) * (n//b+1) + max((b-1) - max(n%b,k-1),0) * (n//b)
    if k==0:
        ans -= 1

print(ans)
