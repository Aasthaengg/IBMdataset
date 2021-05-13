import sys
sys.setrecursionlimit(10**7)

def calcTime(x,n=0):
  if n*(n+1)//2 >= x:
    return n
  else:
    return calcTime(x,n+1)

x = int(input())
print(calcTime(x))