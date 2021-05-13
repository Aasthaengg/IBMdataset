from collections import defaultdict

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

x = readInt()
l = [0]*(x+1)
l[1]=1

for i in range(2,len(l)):
  if l[i]==0:
    j = i*i
    while 1:
      if j>len(l)-1:
        break
      else:
        l[j]=1
        j*=i


for i in range(len(l)-1,-1,-1):
  if l[i]==1:
    print(i)
    break