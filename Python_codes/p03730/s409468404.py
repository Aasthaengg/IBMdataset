from collections import defaultdict

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

a,b,c = readInts()

i = a
his = []
while 1:
  if i%b==c:
    print("YES")
    exit()
  else:
    if i%b in his:
      print("NO")
      exit()
    else:
      his.append(i%b)
      i+=a

