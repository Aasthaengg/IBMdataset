n=int(input())
cnt=0

def check(v,n):
  if len(n) > len(v):
    return 10**(len(v)-2)
  if len(n) < len(v):
    return 0
  if n[0] > v[-1]:
    return 10**(len(v)-2)
  if n[0] == v[-1]:
    x=1 if v[0] > n[-1] else 0
    return max(0, int(n[1:-1])-x+1)
  if n[0] < v[-1]:
    return 0

for i in range(1,n+1):
  st=str(i)
  nst=str(n)
  if st[-1]=='0':
    continue
  if len(st) == 1:
    cnt+=1
    continue
  if len(st)==2:
    if int(st[-1]+st[0]) <= n:
      cnt += 1
  else:
    cnt+= check(st,nst)
    for i in range(len(st)-2):
      xst=st[-1]+'9'*i+st[0]
      cnt += check(xst,nst)*2
  if st[0]==st[-1]:
    cnt += 2

print(cnt)