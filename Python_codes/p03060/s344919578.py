import itertools

n=int(input())
lis=[list(map(int,input().split())) for _ in range(2)]
ans=0

for li in itertools.product([0,1], repeat=n):
  v=0
  for id,l in enumerate(li):
    if l:
      v += lis[0][id] - lis[1][id]
      
  if v > ans:
    ans=v
    
print(ans)