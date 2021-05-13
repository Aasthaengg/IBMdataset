n = int(input())
d = {}
for i in range(n):
  s,p = input().split()
  if d.get(s,-1)==-1:
    d[s] = {int(p):i+1}
  else:
    d[s][int(p)] = i+1
d = sorted(d.items(), key=lambda x:x[0])
for k in d:
  l = sorted(k[1].items(), key=lambda x:x[0])[::-1]
  for t in l:
    print(t[1])