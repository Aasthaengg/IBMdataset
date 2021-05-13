from collections import defaultdict
import itertools
import copy

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

h,w = readInts()
s = [list(input()) for i in range(h)]

for i in range(1,w-1):
  for j in range(1,h-1):
    if s[j][i]=="#":
      c = 0
      if s[j-1][i]=="#":
        c+=1
      if s[j+1][i]=="#":
        c+=1
      if s[j][i-1]=="#":
        c+=1
      if s[j][i+1]=="#":
        c+=1
      if c==0:
        print("No")
        exit()

print("Yes")