n=int(input())
p=list(map(int,input().split()))
q=sorted(p)
ans=0
for i in range(len(p)):
    if p[i]!=q[i]:
        ans=ans+1
if ans>2:
    print("NO")
else:
    print("YES")