a,b,k = map(int,input().split())
ans = set()
if b-a+1 < k:
    for m in range(a,b+1):
        ans.add(m)
else:
    for i in range(a,a+k):
        ans.add(i)
    for j in range(b,b-k,-1):
        ans.add(j)

ans = list(ans)
ans.sort()
for l in range(len(ans)):
    print(ans[l])