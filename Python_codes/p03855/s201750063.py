def root(x,par):
    if x == par[x]:
        return x
    else:
        par[x] = root(par[x],par)
        return par[x]
 
def unite(x,y,par):
    x = root(x,par)
    y = root(y,par)
    if x==y:
        if x==0 and y==1:
            return
    else:
        par[x]=y

n,k,l = map(int,input().split())
road =[i for i in range(n)]
train = [i for i in range(n)]
ans =0
for _ in range(k):
    p,q = map(int,input().split())
    unite(p-1,q-1,road)
for _ in range(l):
    p,q = map(int,input().split())
    unite(p-1,q-1,train)

for i in range(n):
    root(i,train)
for i in range(n):
    root(i,road)

dual = [(i,j) for i,j in zip(road,train)]
ans ={}
for i in dual:
    if i in ans:
        ans[i] +=1
    else:
        ans[i] =1
for i in dual:
    print(ans[i],end=" ")
    
