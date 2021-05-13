N = int(input())
array = list(map(int,input().split()))
product =  1
if 0 in array:
  print(0)
  exit()
for i in array:
  product *= i
  if product > 10**18:
    print(-1)
    exit()
print(product)