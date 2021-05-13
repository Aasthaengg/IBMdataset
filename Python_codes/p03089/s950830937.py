N=int(input())
b=list(map(int,input().split()))
ans=[]
for i in range(N):
    n=len(b)
    cond=True
    for j in range(n):
        if n-j==b[n-j-1]:
            del b[n-j-1]
            ans.append(n-j)
            cond=False
            break
    if cond:
        ans=[-1]
        break
for a in range(len(ans)):
    print(ans[len(ans)-a-1])