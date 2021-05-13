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

ma = max(a)
ans = 0
seki = 1
for i in a:
  seki*=i

for i in a:
  ans += (seki-1)%i

print(ans)