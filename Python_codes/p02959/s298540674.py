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
b = readInts()
b.append(0)
b.append(0)

s = sum(a)

for i in range(n+1):
  if a[i]>=b[i]:
    a[i]-=b[i]
  else:
    b[i]-=a[i]
    a[i] = 0
    a[i+1] = max(0,a[i+1]-b[i])

print(s-sum(a))