n,m,x,y = map(int,input().split())
a = list( map(int,input().split()) )
b = list( map(int,input().split()) )

ck = 0
ans = 0
for z in range(x+1,y+1):
  for i in a:
    if not i < z:
      break 
  else:
    for i in b:
      if not i >= z:
        break
    else:
      ck = 1
      ans = z
      break

print('No War' if ck else 'War')