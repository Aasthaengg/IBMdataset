n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
  if a[i]%2==0:
    if a[i]%3 !=0:
      if a[i]%5 !=0:
        b.append(0)
        break
if 0 in b:
  print('DENIED')
else:
  print('APPROVED')