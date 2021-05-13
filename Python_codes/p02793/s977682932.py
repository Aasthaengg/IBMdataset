N = int(input())
As = list(map(int, input().split()))

def calcgcd(a, b):
  if a > b:
    a, b = b, a
  while a > 0:
    a, b = b%a, a
  return b
def calclcm(a, b):
  return a*b//calcgcd(a, b)

r = 1
a = As[0]
for i in range(1, N):
  b = As[i]
  d = calcgcd(a, b)
  r = (r*(b//d)+(a//d))%1000000007
  a = a*b//d
print(r)
