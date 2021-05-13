n=int(input())
s=''
while n!=0:
  s=str(n%2)+s
  n=-(n//2)
if s!='':
  print(s)
else:
  print(0)
