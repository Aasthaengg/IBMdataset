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
if len(s)%2==1:
  s = s[:-1]
else:
  s = s[:-2]
while 1:
  if s[:len(s)//2]==s[len(s)//2:]:
    print(len(s))
    exit()
  else:
    s = s[:-2]