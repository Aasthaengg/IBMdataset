n,m=map(int,input().split())
lst=[]
for i in range(n):
    a=list(map(int,input().split()))
    lst.append(a)
    
lst=sorted(lst,key=lambda x:x[0])
ans=0
for i in range(n):
    honsuu=lst[i][1]
    if honsuu>=m:
        ans+=(m*lst[i][0])
        break
    else:
        m-=honsuu
        ans+=(honsuu*lst[i][0])

print(ans)