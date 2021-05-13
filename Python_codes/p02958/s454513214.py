n=int(input())
p=[int(j) for j in input().split()]
s=range(n+1)
x=0
  
c=0

for a in range(n):
  if p[a]!=s[a+1]:
    c=c+1
  

if c>2:
  print('NO')
  
if c<=2:
  print('YES')