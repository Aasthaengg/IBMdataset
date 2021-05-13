n = int(input())
b = n%2
print(n*(n-1)//2 - n//2)
for i in range(1, n):
  for j in range(i+1, n+1):
    if i+j+b != n+1:
      print(i, j)