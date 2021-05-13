X = int(input())

count = X // 100
mod = X % 100

if mod <= count*5:
  print(1)
else:
  print(0)