N = int(input())

from collections import defaultdict
d = defaultdict(int)
cnt = 0
for i in range(N):
  s = input().replace("AB","#")
  cnt += s.count("#")
  l = 1 if s[0]  == "B" else 0
  r = 1 if s[-1] == "A" else 0
  d[(l,r)] += 1

if d[(1,0)]>0  and d[(0,1)]>1 :
  print(cnt+d[(1,1)] + min(d[(0,1)],d[(1,0)]))
elif d[(1,0)] >0 or d[(0,1)]>0:
  print(cnt+d[(1,1)] + min(d[(0,1)],d[(1,0)]))
else:
  print(cnt+max(0,d[(1,1)]-1))
  
  
