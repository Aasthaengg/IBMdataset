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

ans = 0
for i in a:
  ans+=i-1
print(ans)