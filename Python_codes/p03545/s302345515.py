a=input()
n=len(a)

for i in range(2**n):
  res=int(a[0])
  ans=[a[0]]
  for j in range(1,n):
    if i&(1<<j):
      ans.append('+')
      ans.append(a[j])
      res+=int(a[j])
    else:
      ans.append('-')
      ans.append(a[j])
      res-=int(a[j])
  if res==7:
    print(*ans,'=7',sep='')
    exit()