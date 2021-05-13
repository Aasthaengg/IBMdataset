import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
 
n = int(readline())
a = list(map(int,readline().split()))

b = [0]*(n+1)
b[-1] = a[-1]
for i in range(n-1,-1,-1):
  b[i] = b[i+1]+a[i]
#print(b)
c = [1]*(n+1)
for i in range(n):
  c[i+1] = (c[i]-a[i])*2
#print(c)
ans = 0
for i in range(n+1):
  m = min(b[i],c[i])
  ans += m
  
if m < 0 or a[0] != 0 or c[-1] < a[-1]:
  ans = -1

if n == 0 and a[0] == 1:
  ans = 1
  
print(ans)