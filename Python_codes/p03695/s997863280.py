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
a = readInts()
rate = [0]*9


for i in a:
  rate[min(i//400,8)]+=1
base = 8-rate[:-1].count(0)
ma = base+rate[-1]
print(max(base,1),ma)
