import collections as cl
h,w,n = map(int,input().split())
l = []
for i in range(n):
  a,b = map(int,input().split())
  for i in range(3):
    x = a+(i-1)
    if x in [0,1,h,h+1]:
      continue
    for j in range(3):
      y = b+(j-1)
      if y in [0,1,w,w+1]:
        continue
      l.append((x-1)*w+y)
#print(l)
p = cl.Counter(l)
q = cl.Counter(p.values())
print((h-2)*(w-2)-sum(q.values()))
for i in range(1,10):
  if i in q.keys():
    print(q[i])
  else:print(0)