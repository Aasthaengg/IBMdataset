def calcgcd(a, b):
  if a > b:
    a, b = b, a
  while a > 0:
    a, b = b%a, a
  return b
def calclcm(a, b):
  return a*b//calcgcd(a, b)

A, B = map(int, input().split())
r = calclcm(A, B)
print(r)
