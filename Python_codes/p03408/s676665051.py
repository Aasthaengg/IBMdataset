d={}
r=[input() for _ in range(int(input()))]
for _ in range(int(input())):
  a=input()
  if a in r:
    r.pop(r.index(a))
for i in r:
  if i not in d:
    d[i] = 1
  else:
    d[i] += 1
d=sorted(d.items(),key=lambda x:-x[1])
print([0,d[0][1]][d[0][1]>0] if d else 0)