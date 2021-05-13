n,k  = map(int, input().split())

if n == 1:
  number = k
else:
  number = k*(k-1)**(n-1)

print(number)