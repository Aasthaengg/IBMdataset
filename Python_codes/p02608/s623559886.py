n = int(input())
arr = [0] * (n + 1)

for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1, 101):
      a = x**2 + y**2 + z**2 + x*z + y*z + x*y
      if a<= n:
        arr[a] += 1
        
for i in range(1,n+1):
    print(arr[i])