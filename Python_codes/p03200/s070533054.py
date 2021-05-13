from collections import defaultdict

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

s = input()

ans = 0
bCount = 0
for i in s:
  if i=="B":
    bCount += 1
  else:
    ans+=bCount
print(ans)