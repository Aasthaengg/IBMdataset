import math
n,h=map(int,input().split())
furu=[None]*n
nageru=[None]*n
for i in range(n):
    a,b=map(int,input().split())
    furu[i]=a
    nageru[i]=b
rep=max(furu)
nagekaku=[]
for i in range(n):
    if rep<nageru[i]:
        nagekaku.append(nageru[i])
nage_sum=sum(nagekaku)
if nage_sum>=h:
    nagekaku=sorted(nagekaku,reverse=True)
    ans=0
    for i in range(len(nagekaku)):
        h-=nagekaku[i]
        ans+=1
        if h<=0:
            break
else:
    ans=len(nagekaku)
    h-=nage_sum
    ans+=math.ceil(h/rep)

print(ans)