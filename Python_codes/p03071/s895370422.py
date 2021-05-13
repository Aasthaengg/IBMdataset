a,b=map(int,input().split())
l=[a,b]
l.sort()
ans=l[1]
l[1]=l[1]-1
l.sort()
ans+=l[1]
print(ans)