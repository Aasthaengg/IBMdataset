a=int(input())
b=int(input())

ans=1
for _ in range(a):
    ans=min(ans*2,ans+b)
print(ans)