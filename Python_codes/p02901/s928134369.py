n,m=map(int,input().split())
ans=[float("inf")]*(2**n)
ans[0]=0
for i in range(m):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    tmp=0
    for j in c:
        tmp+=2**(j-1)
    na=ans.copy()
    for j in range(2**n):
        if ans[j|tmp]>na[j]+a:
            ans[j|tmp]=na[j]+a
if ans[2**n-1]==float("inf"):
    print(-1)
else:
    print(ans[2**n-1])