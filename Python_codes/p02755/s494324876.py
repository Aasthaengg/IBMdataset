a,b=map(int,input().split())
ans=-1
for i in range(1,10**4):
    if ((i*10)//100)==b and ((i*8)//100)==a:
        ans=i
        break
print(ans)