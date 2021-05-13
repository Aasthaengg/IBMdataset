n = int(input())
a = list(map(int, input().split()))

t = True
x = -1

while t == True:
  x += 1
  for i in a:
    if i%2 == 0:
      continue
    else:
      t = False
  a = list(map(lambda x:x/2, a))  

      
print(x)