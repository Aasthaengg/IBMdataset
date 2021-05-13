n,q=map(int,input().split())
s=list(input())
x=[[] for i in range(q)]
for i in range(q):
    l,r=map(int,input().split())
    x[i].append(l)
    x[i].append(r)
ans=[0 for i in range(n+1)]
if s[0]=="A" and s[1]=="C":
    ans[2]=1
for i in range(3,n+1):
    if s[i-1]=="C" and s[i-2]=="A":
        ans[i]=ans[i-1]+1
    else:
        ans[i]=ans[i-1]
for i in range(q):
    print(ans[x[i][1]]-ans[x[i][0]])
        
