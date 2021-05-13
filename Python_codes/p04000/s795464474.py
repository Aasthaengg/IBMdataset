import collections 
def solve():
  h,w,n = (int(i) for i in input().split())
  
  query = []
  for i in range(n):
    a,b = (int(i) for i in input().split())
    d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    for dx,dy in d:
      if 2 <= a+dx <= h-1 and 2 <= b+dy <= w-1:
        query.append((a+dx,b+dy))
  ans = [0]*10
  if query:
   query = collections.Counter(query)
   values, counts = zip(*query.most_common())
   for i in range(10):
     ans[i] = counts.count(i)
  tp = sum(ans)
  ans[0] = (h-2)*(w-2)-tp
  
  for i in ans:
    print(i)
solve()
