nim,mike = map(int,input().split())
array = []

while nim<=mike:
  array.append(nim)
  nim*=2

print(len(array))