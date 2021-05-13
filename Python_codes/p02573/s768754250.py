n,m=map(int,input().split())
flag=list(range(n+1))
flagnum=[0]*(n+1)

#以下でフラグ建設 フラグが同じなら同じチームである
def takeflag(p):
    stock=[]
    while flag[flag[p]]!=flag[p]:
        stock.append(p)
        p=flag[p]
    p=flag[p]
    for i in stock:
        flag[i]=p
    return p
for i in range(m):
    a,b = map(int,input().split())
    a,b = map(takeflag,(a,b))
    a,b = min(a,b),max(a,b)
    flag[a]=b
for i in range(n+1):
    flag[i]=takeflag(i)
    flagnum[flag[i]]+=1 #チームの人数を知りたいときこの行を使う
print(max(flagnum))