n=int(input())
l=[list(map(int,input().split()))[::-1] for _ in range(n)]
l.sort()
t=0

ans="Yes"
for m in l:
  t+=m[1]
  if t>m[0]:
    ans="No"
print(ans)