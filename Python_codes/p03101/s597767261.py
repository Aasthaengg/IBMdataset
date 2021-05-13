import math
def I():
  return input()
def II():
  return int(input())
def MII():
  return map(int, input().split())
def LMII():
  return list(map(int, input().split()))
def P(s):
  return print(s)

a,b = MII()
h,w=MII()
P((a-h)*(b-w))