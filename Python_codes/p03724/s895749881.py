n,m=map(int,input().split())
l=[0]*(n+1)
for i in range(m):
    a,s=map(int,input().split())
    l[a]+=1
    l[s]+=1
for i in l:
    if i%2:print("NO");exit()
print("YES")