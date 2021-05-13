n,m,q=map(int,input().split())
query=[]
for _ in range(q): query.append(list(map(int,input().split())))
ans=0
def rec(a):
    if len(a)==n+1:
        temp=0
        for qu in query:
            if a[qu[1]]-a[qu[0]]==qu[2]: temp+=qu[3]
        global ans
        ans=max(ans,temp)
        return
    for i in range(a[-1],m+1):
        cp=a[:]
        cp.append(i)
        rec(cp)
rec([1])
print(ans)