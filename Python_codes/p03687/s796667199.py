s = input()
n = len(s)
chk = [[0] for i in range(n)]
cc = set()
d = {}
cnt = 0
for i,si in enumerate(s):
  if not si in cc:
    d[si] = cnt
    cnt += 1
    cc.add(si)
  chk[d[si]].append(i+1)
#print(chk)
ans = n//2
for j in chk:
  p = 0
  j = j + [n+1]
  for k in range(len(j)-1):
    p = max(p,j[k+1]-j[k]-1)
    if p >= ans:
      break
    if k == len(j)-2:
      ans = min(p,ans)
print(ans)