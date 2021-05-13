n,a,b=map(int,input().split())
res=0
for i in range(n+1):
    ans=0
    s=list(str(i))
    for j in s:ans+=int(j)
    if a<= ans <= b:res+=i
print(res)