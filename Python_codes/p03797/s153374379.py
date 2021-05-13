n,m=map(int,input().split())
val=min(n,m//2)
#print(val,end=' val\n')
n-=val
m-=2*val
ans=val
#print(m,end=' m\n')
ans+=m//4
print(ans)

