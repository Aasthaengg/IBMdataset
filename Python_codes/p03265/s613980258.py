from collections import defaultdict

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

x1,y1,x2,y2 = readInts()
dx = x2-x1
dy = y2-y1

print(x2-dy,y2+dx,x1-dy,y1+dx)