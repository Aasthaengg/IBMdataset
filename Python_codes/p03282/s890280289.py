from collections import defaultdict
def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

s = readChar()
k = readInt()
for i in range(k):
  if s[i]!="1":
    print(s[i])
    exit()

print(1)