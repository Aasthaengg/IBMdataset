k,x=map(int,input().split())
ans=[]
for i in range(k):
    if -1000000<=x-i:
        ans.append(x-i)
    ans.append(x)
    if x+i<=1000000:
        ans.append(x+i)
ans=set(ans)
ans=list(ans)
ans=sorted(ans)
for i in range(len(ans)):
    print(ans[i])