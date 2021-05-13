n=[int(s) for s in input().split()]
p=[int(s) for s in input().split()]
count=0
expected=0
a=0
f=0
for i in p:
  if i==a+1:
    a+=1
  else:
    if count>0:
      f=1
    if expected==0:
      expected=i
      a+=1
    else:
      if expected==a+1:
        count+=1
        a+=1
      else:
        f=1

if f==0:
  print('YES')
else:
  print('NO')