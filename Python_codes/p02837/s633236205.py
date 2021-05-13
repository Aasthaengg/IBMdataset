def II(): return int(input())
def MI(): return map(int, input().split())
N=II()
shogens=[]
for i in range(N):
  a=II()
  shogens.append([])
  for j in range(a):
    x,y=MI()
    x-=1
    shogens[-1].append((x,y))
def is_honest(i,j):
  return (i>>j)%2==1
def honest_cnt(i):
  ans=0
  for j in range(N):
    ans+=is_honest(i,j)
  return ans
ans=0
for i in range(1<<N):
  ok=True
  for j in range(N):
    if not is_honest(i,j):
      continue
    for (x,y) in shogens[j]:
      if y==0 and is_honest(i,x):
        ok=False
      if y==1 and not is_honest(i,x):
        ok=False  
  if ok:
    ans=max(ans,honest_cnt(i))
print(ans)