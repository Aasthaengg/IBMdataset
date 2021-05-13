def p(x):
 if x==2:return 1
 if x%2==0:return 0
 i=3
 while i<=x**.5:
  if x%i==0:return 0
  i+=2
 return 1
n=int(input())
print(sum([p(int(input()))for _ in range(n)]))