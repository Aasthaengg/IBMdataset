n = int(input())

if 1<= n <= 9:
  e = n 
  print(e)
elif 10 <= n <= 99:
  print(9)
elif 100 <= n <= 999:
  e = 9 + n - 100 + 1
  print(e)
elif 1000 <= n <= 9999:
  e = 909 
  print(e)
elif 10000 <= n <= 99999:
  e = 909 + n - 10000 + 1
  print(e)
elif n == 100000:
  print(90909)