x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
ans=[]
s=x+y
for i in p:
    ans.append((i,0))
for i in q:
    ans.append((i,1))
for i in r:
    ans.append((i,2))
ans.sort(reverse=True)
res=0
cnt=0
for i , j in ans:
    if j==0:
        if x>0:
            x-=1
            cnt+=1
            res+=i
    elif j==1:
        if y>0:
            y-=1
            cnt+=1
            res+=i
    else:
        cnt+=1
        res+=i
    if cnt>=s:
        break

print(res)
