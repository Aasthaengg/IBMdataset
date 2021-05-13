def check(a,b):
  d=[]
  for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
      d.append(i)
  return d[::-1]
a,b,k=map(int,input().split())
print(check(a,b)[k-1])