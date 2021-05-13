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

num = [0,0]
for i in s:
  num[i]+=1
print(min(num)*2)