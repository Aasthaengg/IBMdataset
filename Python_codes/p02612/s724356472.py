n = int(input())
n %= 1000
n = 1000 - n
if n == 1000:
  n = 0
print(n)