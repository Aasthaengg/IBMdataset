import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline()[:-1]
mod = 10**9 + 7
def readInt():return int(input())
def readIntList():return list(map(int,input().split()))
def readStringList():return list(input())
def readStringListWithSpace():return list(input().split())
def readString():return input()

days = readString()
if 'RRR' in days:
  print(3)
elif 'RR' in days:
  print(2)
elif 'R' in days:
  print(1)
else:
  print(0)

# readStringList()
# count = 0
# res = 0
# for c in days:
#     count += 0 if c == 'S' else 1
#     res = max(res,count)
# print(res)