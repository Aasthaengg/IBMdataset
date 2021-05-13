n=int(input())
if n==1 or n==2:
  print(0)
  exit()
d=0
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    if i!=n//i and i!=n//i-1:
      d=d+n//i-1
print(d)