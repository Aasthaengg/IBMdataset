n=int(input())
ans=float(0)
for i in range(0,n):
    x,u=input().split()
    if u=="JPY":
        ans=ans+float(x)
    else:
        ans=ans+float(float(x)*380000)
print(ans)