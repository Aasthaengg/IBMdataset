n,*a=map(int,open(0).read().split())
i=ans=1
while a[i-1]!=2 and ans<=n:
    ans+=1
    i=a[i-1]
print(ans if ans<=n else -1)