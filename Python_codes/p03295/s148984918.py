# kaisetsu
n,m=map(int,input().split())
ab=[tuple(map(int,input().split())) for _ in range(m)]
ab.sort(key=lambda x:x[1])
# print(ab)
ans=0

right=-1
for a,b in ab:
  if a<right:
    continue
  ans+=1
  right=b
print(ans)