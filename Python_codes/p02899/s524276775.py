n=int(input())
ans=[[] for i in range(n)]
a=list(map(int,input().split()))
for i in range(n):
    ans[i].append(a[i])
    ans[i].append(i+1)
ans=sorted(ans)
x=[]
for i in range(n):
    x.append(str(ans[i][1]))

print(" ".join(x))
