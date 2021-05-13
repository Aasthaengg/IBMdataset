n,h=map(int,input().split())
p=[]
for i in range(n):
    a,b=map(int,input().split())
    p.append([a,0])
    p.append([b,1])

p=sorted(p,key=lambda x:-x[0])

i=0
ans=0
while h>0:
    if p[i][1]==1:
        h-=p[i][0]
        ans+=1
        i+=1
    else:
        ans-=(-h//p[i][0])
        break

print(ans)
