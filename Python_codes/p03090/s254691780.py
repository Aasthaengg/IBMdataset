n = int(input())

sm = n*(n+1)//2
if n == 3:
  print(2)
  print(1, 3)
  print(2, 3)
elif n == 4:
  print(4)
  print(1, 2)
  print(1, 3)
  print(2, 4)
  print(3, 4)
elif n % 2:
  m = (n-1)//2
  print(m*4)
  a = [[i, n-i-2] for i in range(m)]
  for i in range(m-1):
    for j in range(2):
      for k in range(2):
        print(a[i][j]+1, a[i+1][k]+1)
  for i in range(2):
    print(a[m-1][i]+1, n)
    print(n, a[0][i]+1)
else:
  print(n*2)
  a = [[i, n-i-1] for i in range(n//2)]
  for i in range(n//2):
    for j in range(2):
      for k in range(2):
        print(a[i][j]+1, a[(i+1)%(n//2)][k]+1)