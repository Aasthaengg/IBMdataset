n=int(input())
if n % 2 == 0:
  temp = int(n/2)
  print(temp ** 2)
else:
  temp = n//2
  print(temp*(temp+1))