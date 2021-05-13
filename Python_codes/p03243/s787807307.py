N = int(input())

def checkDigit(n):
  a = n % 10
  n = (n-a)//10
  b = n % 10
  c = (n-b)//10
  if a == b and b == c:
    return True
  else:
    return False

for i in range(1000):
  if checkDigit(N):
    print(N)
    break
  N += 1