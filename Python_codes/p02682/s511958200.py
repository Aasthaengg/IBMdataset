import sys
def Ii():return int(sys.stdin.buffer.read())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))
 
a,b,c,k = Mi()
if k <= a:
  print(k)
  exit(0)
ans = a
k -= a
if k > b:
  ans -= k-b
  
print(ans)