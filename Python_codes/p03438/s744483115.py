n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

sa=[a[i]-b[i] for i in range(n)]

p=0
m=0
for i in sa:
  if 0<i:
    m+=i
  else:
    p+=abs(i)//2

if m<=p:
  print("Yes")
else:
  print("No")