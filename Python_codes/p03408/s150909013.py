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
s = [input() for i in range(n)]
m = readInt()
t = [input() for i in range(m)]

ans = 0
for i in s:
  ans = max(ans,s.count(i)-t.count(i))
print(ans)