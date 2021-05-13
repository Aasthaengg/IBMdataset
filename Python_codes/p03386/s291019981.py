a,b,k = map(int,input().split())
ans = set()

if(b-a <= k-1):
    for i in range(a,b+1):
        ans.add(i)
else:
    for i in range(a,a+k):
        ans.add(i)

    for i in reversed(range(b-k+1,b+1)):
        ans.add(i)

ans = list(ans)
ans.sort()

for i in range(len(ans)):
  print(ans[i])