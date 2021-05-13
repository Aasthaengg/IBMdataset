A,B,K=map(int,input().split())
ans=[]

for i in range(1,101):
    if A%i==0 and B%i==0:
        ans.append(i)

ans=sorted(ans,reverse=True)
print(ans[K-1])