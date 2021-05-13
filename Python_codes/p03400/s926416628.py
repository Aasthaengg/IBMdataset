n = int(input())
d, x = map(int, input().split())
a = list([int(input()) for i in range(n)])

c = 0

for i in range(n):
  cd = 0
  count = 1
  for j in range(d):
    if cd + a[i] <= d - 1:
      cd = cd + a[i]
      count += 1
  
  c = c+count
    
print(c + x)