import sys
input=sys.stdin.readline   #input高速化 １文字の時の改行文字に注意+

d={i:0 for i in range(3001)}
db={i:0 for i in range(3001)}

n,t=map(int,input().split())

x=[tuple(map(int,input().split()))for i in n*[0]]
x.sort()
dp=[]
dp2=[]
for time,value in x:
    for k,v in d.copy().items():
        if k+time<t:
            if d[k+time]<v+value:
                d[k+time]=v+value
        else:
            break
    l=[0]
    for i in range(1,t+1):
        if d[i]>l[-1]:
            l.append(d[i])
        else:
            l.append(l[-1])

    dp.append(l)    
        
for time,value in x[::-1]:
    for k,v in db.copy().items():
        if k+time<t:
            if db[k+time]<v+value:
                db[k+time]=v+value
        else:
            break

    l=[0]
    for i in range(1,t+1):
        if db[i]>l[-1]:
            l.append(db[i])
        else:
            l.append(l[-1])
        
    dp2.append(l)
dp=[[0]*t,[0]*t]+dp
dp2=([[0]*t,[0]*t]+dp2)[::-1]

ans=0

for i in range(len(dp)):
    for j in range(t):
        if i==0 or i==len(dp)-1:
            tmp=dp[i][j]+dp2[i][t-j-1]
            if ans<tmp:
                ans=tmp
        else:
            tmp=dp[i][j]+dp2[i][t-j-1]+x[i-1][1]
            if tmp>ans:
                ans=tmp
print(ans)