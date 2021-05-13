
x = int(input())
 
def calc(n):
  if n == 0:
    return 0
  elif n < 7:
    return 1
  elif n < 12:
    return 2
  else:
    return (n // 11)*2 + calc(n % 11)

print(calc(x))