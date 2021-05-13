n,m=map(int,input().split())
py=[list(map(int,input().split()))+[i] for i in range(m)]

py.sort(key=lambda x:x[0]*10**6+x[1])
ne=[1]*(10**5+1)
ans=[]

for p,_,i in py:
    ans.append((str(p).zfill(6)+str(ne[p]).zfill(6),i))
    ne[p]+=1

ans.sort(key=lambda x:x[1])
for s,_ in ans:
    print(s)