n = int(input())
l = [int(input()) for i in range(2) if n == 2]

if n == 1:
  print('Hello World')
else:
  print(sum(l))