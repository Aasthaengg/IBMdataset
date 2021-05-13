from collections import defaultdict

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

ans = -1

n = readInt()
s = input()

for i in range(1,n):
  a = set(s[:i])
  b = set(s[i:])
  ans = max(ans,len(a&b))

print(ans)