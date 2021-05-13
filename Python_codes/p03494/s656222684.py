import sys 
n = int(input())
num = [int(x) for x in input().split()]
t = 0 
while True: 
  for i in range(n):
    if num[i]%2 == 0:
      num[i] //= 2 
    else:
      print(t)
      sys.exit()
  t += 1