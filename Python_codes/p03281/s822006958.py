N = int(input())

a = 0 

for n in range(1, N+1):
  num = 0
  for i in range(1, n+1):
    if n % i == 0:
      num += 1
  
  if n % 2 == 1 and num == 8:
    a += 1

print(a)