a,b,c=map(int,input().split())
ans=0
for s in range(a):
    d,e=map(int,input().split())
    if b<=d and c<=e:
        ans+=1
print(ans)