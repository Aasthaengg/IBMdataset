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
s = defaultdict(int)
for i in range(n):
  s[input()]+=1
m = readInt()
t = defaultdict(int)
for i in range(m):
  t[input()]+=1

ans = 0
for i in s:
  ans = max(ans,s[i]-t[i])
print(ans)