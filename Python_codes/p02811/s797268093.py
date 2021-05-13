k,x = map(int,input().split())
y = 'Yes'
n = 'No'
if (500*k) < x:
  print(n)
elif (500*k) >= x:
  print(y)