N = int(input())

def num(i):
 num = []
 n = i
 while n != 0:
  num.append(n % 10)
  n = n // 10
 return 3 in num

for i in range(1, N+1):
 if i % 3 == 0:
  print(" " + str(i), end="")
 elif num(i):
  print(" " + str(i), end="")
print("")