n =  int(input())
a = [int(input()) for i in range(5)]
mina = min(a)

repeat = n//mina

if n % mina == 0:
  print(repeat + 4)
else:
  print(repeat + 5)
  
  
