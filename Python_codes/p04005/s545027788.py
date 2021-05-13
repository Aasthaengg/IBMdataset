from collections import defaultdict

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

a,b,c = readInts()

if a*b*c%2==0:
  print(0)
  exit()

x = min(a,b,c)
y = (a+b+c)-x-max(a,b,c)
print(x*y)