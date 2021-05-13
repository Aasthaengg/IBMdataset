import sys
def Ii():return int(sys.stdin.buffer.readline())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

a,b,n = Mi()
if b-1 < n:
  print((a*(b-1))//b)
else:
  print((a*n)//b)