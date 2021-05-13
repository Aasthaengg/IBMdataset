x = int(input())
if x == 2 or x == 3:
   print(x)
   exit()
while True:
      n = 0
      for i in range(2, int(-(-x**0.5//1))+1):
          if x % i == 0:
             break
          else:
              n = n + 1
      if n == int(-(-x**0.5//1))-1 :
          print(x)
          exit()
      else:
          x = x + 1