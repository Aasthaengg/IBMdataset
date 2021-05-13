n,*a=map(int,open(0).read().split())
ans=0
for k,v in enumerate(a):
    if k+1==a[v-1]:
        ans+=1
print(ans//2)
