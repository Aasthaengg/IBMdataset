n=int(input())

def f(x):
  m=int(x**(1/2))
  ret=set()
  for i in range(1,m+1):
    if x%i==0:
      ret.add(i)
      ret.add(x//i)
  return ret


ans=set()
for i in f(n):
  if i==1:
    continue
  g=n
  while g%i==0:
    g=g//i
  if g%i==1:
    ans.add(i)

for j in f(n-1):
  if j==1:
    continue
  if j in ans:
    continue
  ans.add(j)
  
print(len(ans))