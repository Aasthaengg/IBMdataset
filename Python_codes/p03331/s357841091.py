n = int(input())

ans=10**9+7
for i in range(1,n):
    tmp=list(str(i)) + list(str(n-i))
    tmp=[int(i) for i in tmp]
    ans=min(ans, sum(tmp))

print(ans)