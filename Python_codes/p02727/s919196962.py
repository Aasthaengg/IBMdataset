x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r+=p[:x]+q[:y]
r.sort(reverse=True)
ans=0
for i in range(x+y):
    ans+=r[i]
print(ans)
