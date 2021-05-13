N=int(input())
print(0)
s=input()
if s=='Vacant':
  exit()
x=s
print(N-1)
s=input()
if s=='Vacant':
  exit()
left=0
right=N
while True:
  n=(left+right)//2
  print(n)
  s=input()
  if s=='Vacant':
    exit()
  if n%2!=0:
    if s==x:
      right=n
    else:
      left=n
  else:
    if s!=x:
      right=n
    else:
      left=n
