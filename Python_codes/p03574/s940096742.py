from collections import defaultdict

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

for i in range(h):
  for j in range(w):
    if s[i][j]=="#":
      if i!=0:
        if j-1>=0:
          if s[i-1][j-1]==".":
            s[i-1][j-1] = 1
          elif s[i-1][j-1]!="#":
            s[i-1][j-1]+=1
        if s[i-1][j]==".":
          s[i-1][j] = 1
        elif s[i-1][j]!="#":
          s[i-1][j]+=1
        if j+1<=w-1:
          if s[i-1][j+1]==".":
            s[i-1][j+1] = 1
          elif s[i-1][j+1] != "#":
            s[i-1][j+1]+=1
      if j-1>=0:
        if s[i][j-1]==".":
          s[i][j-1] = 1
        elif s[i][j-1]!="#":
          s[i][j-1]+=1
      if j+1<=w-1:
        if s[i][j+1]==".":
          s[i][j+1] = 1
        elif s[i][j+1] != "#":
          s[i][j+1]+=1
      if i+1<=h-1:
        if j-1>=0:
          if s[i+1][j-1]==".":
            s[i+1][j-1] = 1
          elif s[i+1][j-1]!="#":
            s[i+1][j-1]+=1
        if s[i+1][j]==".":
          s[i+1][j] = 1
        elif s[i+1][j]!="#":
          s[i+1][j]+=1
        if j+1<=w-1:
          if s[i+1][j+1]==".":
            s[i+1][j+1] = 1
          elif s[i+1][j+1] != "#":
            s[i+1][j+1]+=1

for i in s:
  for j in i:
    if j==".":
      print("0",end="")
    else:
      print(j,end="")
  print()