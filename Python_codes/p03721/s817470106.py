n,k=map(int,input().split())
ans=[0]*(10**5+1)
for i in range(n):
    a,b=map(int,input().split())
    ans[a]+=b
    
v=0
for i in range(k):
    v+=ans[i]
    if ans[i]==0:
        i-=1
    if v>=k:
        a=i
        break
    
print(a)