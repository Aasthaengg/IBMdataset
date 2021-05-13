from collections import defaultdict
def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

n = readInt()
a = 1
for i in range(2,n+1):
  a = (a*i)%(10**9+7)
print(a)