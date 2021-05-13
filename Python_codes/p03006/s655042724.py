n=int(input())
ans=n
l=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:continue
        p,q=l[i][0]-l[j][0],l[i][1]-l[j][1]
        ret=0
        pre=sorted(l,reverse=1,key=lambda x:p*x[0]+q*x[1])
        while pre:
            ret+=1
            x,y=pre.pop()
            while  [x+p,y+q] in pre:
                pre.remove([x+p,y+q])
                x,y=[x+p,y+q]
        ans=min(ans,ret)
print(ans)