N,M=map(int, input().split())

B=[]
for i in range(M):
    a,b=map(int, input().split())
    B.append((a,b))


B=sorted(B)
now=-1
pre=1
ans=0
for i in range(M):
    
    left,right=B[i]
    if i==0:
        now=left
        pre=right
        if i==M-1:
            ans+=1
        continue
    if i==M-1:
        ans+=1
    if now!=left and pre<=left:
        now=left
        ans+=1
        pre=right
    elif now!=left and pre>left:
        pre=min(pre,right)
        continue
    elif now==left:
        pre=min(pre,right)
    

print(ans)
#print(B)