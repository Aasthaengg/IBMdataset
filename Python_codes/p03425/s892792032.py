n = int(input())

march = ("M","A","R","C","H")
prefix = []
d = {}
for _ in range(n):
  pre = input()[0]
  if pre in march:
    if pre not in prefix:
      prefix.append(pre)
      d[pre] = 1
    else:
      d[pre] += 1
      
t = len(prefix)
if t < 3:
  print(0)
  exit()

ans = 0
for i in range(t-2):
  for j in range(i+1, t-1):
    for k in range(j+1,t):
      ans += d[prefix[i]]*d[prefix[j]]*d[prefix[k]]
print(ans)