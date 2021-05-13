n=int(input())
p=list(map(int,input().split()))
ok=True
for i in range(1,n):
  if p[i]-p[i-1]>0:
    continue
  ok=False
if ok:
  print("YES")
  exit(0)

for i in range(n):
  for j in range(n):
    if i==j:continue
    t=p[:]
    taihi=t[i]
    t[i]=t[j]
    t[j]=taihi
    ok=True
    for k in range(1,n):
      if t[k]-t[k-1]>0:
        continue
      ok=False
    if ok:
      print("YES")
      exit(0)
print("NO")

