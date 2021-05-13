n, x = map(int,input().split())
children = list(map(int,input().split())) 
children.sort()
count=0
c = 0
if x < children[0]:
  print(0)
  exit()
for i in range(n):
  count += children[i]
  c += 1
  if count == x:
    print(c)
    exit()
  elif count > x:
    print(c-1)
    exit()

print(n-1)
