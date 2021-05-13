from collections import defaultdict as ddict
d = (-1,0,1)
cmap = ddict(int)
h,w,n = map(int, input().split())
for _ in range(n):
  a,b = map(int, input().split()) 
  for x in d:
    for y in d:
      ca = a+x
      cb = b+y
      if 1<ca<h and 1<cb<w:
        cmap[(ca,cb)] += 1
l = [0]*10
j = list(cmap.values())
for i in range(1,10):
  l[i] = j.count(i)
l[0] = (h-2)*(w-2) - sum(l)
for x in l:
  print(x)