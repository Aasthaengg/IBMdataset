h = int(input())
w = int(input())
n = int(input())

if h >= w:
  if n%h == 0:
    print(str(n//h))
  else:
    print(str(n//h+1))
else:
  if n%w == 0:
    print(str(n//w))
  else:
    print(str(n//w+1))
  
