import sys
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.readline().split())
def Li():return list(map(int,sys.stdin.readline().split()))

x,y = Mi()
if y%2 == 1:
  print('No')
  exit(0)
  
y = y//2

if x <= y <= 2*x:
  print('Yes')
else:
  print('No')