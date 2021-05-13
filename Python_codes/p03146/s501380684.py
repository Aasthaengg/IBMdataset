s=int(input())
if 1==s or 2==s or 4==s:
  print(4)
  exit()
x=0
for i in range(1,10**9):
  if 1==i:
    x=s
  if 1<i:
    if x%2!=0:
      x=3*x+1
    else:
      x/=2
  if 4==x:
    print(i+3)
    exit()
