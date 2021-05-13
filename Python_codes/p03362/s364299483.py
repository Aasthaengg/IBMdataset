def check(x):
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return False
  return True
n=int(input())
l=[]
for i in range(11,55551,10):
  if check(i):
    l.append(i)
print(*l[:n])