n=int(input())
a=0
for i in range(n):
  m, curr=input().split()
  m=float(m)
  curr=str(curr)
  if curr=='BTC':
    a=a+m*380000
  else:
    a=a+m
print(a)
