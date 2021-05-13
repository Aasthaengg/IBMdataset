n,k=map(int,input().split())
s=[[]for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    s[a].append(b)
    s[b].append(a)
d=[False]*(n+1)
q=[[0,1]]
c=0
a=k
while q:
    t=[]
    c=0
    for i,j in q:
        c=0
        for p in s[j]:
            if p!=i:
                t.append([j,p])
                c+=1
        r=(k-1 if j==1 else k-2)
        for h in range(r,r-c,-1):
            a=(a*h)%(10**9+7)
    q=t
print(a)