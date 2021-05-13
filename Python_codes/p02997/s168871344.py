n,k = map(int,input().split())
if n == 2 and k == 0:
  print(1)
  print(1,2)
  exit()
  
if k > (n-1)*(n-2)//2 or n == 2:
  print(-1)
  exit()
  
if n == 3:
  if k == 1:
    print(2)
    print(1,2)
    print(2,3)
  elif k == 0:
    print(3)
    print(1,2)
    print(2,3)
    print(3,1)
  else:
    print(-1)
  exit()
    
m = (n-1)*(n-2)//2+(n-1)-k
print(m)
for i in range(n-1):
  print(1,2+i)
for i in range(min(n-1,m-n+1)):
  if 3+i > n:
    print(2+i,2)
  else:
    print(2+i,3+i)
    
if m > (n-1)*2:
  cnt = m-(n-1)*2
  for i in range(2,n-2):
    if cnt == 0:
        break
    for j in range(2,n-i+1):
      print(j,j+i)
      cnt -= 1
      if cnt == 0:
        break