n,k=map(int, input().split())
v=list(map(int, input().split()))

r=min(n,k)
ans=0

for a in range(r+1):
    for b in range(r+1):
        jew=[]
        if a+b>r:
            break
        for i in range(a):
            jew.append(v[i])
        for i in range(n-1,n-b-1,-1):
            jew.append(v[i])
        
        if len(jew)==0:
            continue

        jew.sort(reverse=True)

        for i in range(k-(a+b)):
            if len(jew)>0:
                if jew[-1]<0:
                    jew.pop(-1)
                else:
                    break
        ans=max(ans,sum(jew))
print(ans)
