from collections import defaultdict

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

s = list(map(int,list(input())))

d = [-1]
ans = 0
for i in s:
  if d[-1]+i==1:
    del d[-1]
    ans+=1
  else:
    d.append(i)
print(ans*2)