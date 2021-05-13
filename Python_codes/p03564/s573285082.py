n,k=[int(input()) for _ in range(2)]
ans=1
for _ in range(n):
    ans=min(ans*2,ans+k)
print(ans)

