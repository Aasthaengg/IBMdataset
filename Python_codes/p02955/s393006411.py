def factors(n):
  a = [1,n]
  x = 2
  while x * x <= n :
    if n % x == 0:          
      a.append(x)
      c=n//x
      while(c+1)*x<=n:
        c+=1
      a.append(c)
    x+=1
  return a
n,k=map(int,input().split())
a=list(map(int,input().split()))
candidates=factors(sum(a))
candidates.sort()
candidates.reverse()
for i in candidates:
  b=[]
  for j in range(n):
    b.append(a[j]%i)
  b.sort()
  upsum=0
  downsum=0
  for j in range(n):
    upsum+=i-b[j]
  for j in range(n):
    upsum-=i-b[j]
    downsum+=b[j]
    if upsum<=downsum:
      break
  if upsum<=k:
    print(i)
    break