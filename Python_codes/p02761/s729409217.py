n,m=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(m)]
ans=-1
if n>=2:
  for i in range(10**(n-1),10**n):
    k=['0']+list(str(i))
    judge=True
    for j in lst:
      if k[j[0]]!=str(j[1]):
        judge=False
        break
    if judge:
      ans=i
      break

elif n==1:
  for i in range(10):
    k=['0']+list(str(i))
    judge=True
    for j in lst:
      if k[j[0]]!=str(j[1]):
        judge=False
        break
    if judge:
      ans=i
      break
print(ans)
