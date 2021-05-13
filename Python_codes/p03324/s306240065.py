from collections import defaultdict
def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

d,n = readInts()

if d==0:
  if n==100:
    print(101)
  else:
    print(n)
elif d==1:
  if n==100:
    print(10100)
  else:
    print(n*100)
else:
  if n==100:
    print(1010000)
  else:
    print(n*10000)