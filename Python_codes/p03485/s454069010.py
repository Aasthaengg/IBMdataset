import sys
input = sys.stdin.readline
#-------------
a,b = map(int,input().split())
#-------------
x = (a+b)/2
y = x//1
mod = x%1
if mod == 0:
  print(int(y))
else:
  print(int(y+1))