from operator import itemgetter
n,k = map(int,input().split())
li=[]
s=[]
t=[]
g=0
ans=[]
retu=[0]*n
p=0
q=0
for _ in range(n):
    a,b=map(int,input().split())
    li.append([a,b])
li=sorted(li,key=itemgetter(1),reverse=True)
for i in range(k):
    g+=li[i][1]
    if retu[li[i][0]-1]==0:
        retu[li[i][0]-1]+=1
        p+=1
    else:
        t.append(li[i][1])
        q+=1
g+=p**2
ans.append(g)
for i in range(k,n):
    if q==0:
        break
    if retu[li[i][0]-1]==0:
        g=g-t[q-1]+li[i][1]+2*p+1
        p+=1
        q-=1
        ans.append(g)
        retu[li[i][0]-1]+=1
print(max(ans))