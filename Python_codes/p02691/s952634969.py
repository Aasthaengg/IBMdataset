import sys
def Ii():return int(sys.stdin.buffer.readline())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

n = Ii()
a = Li()
x = [0]*n
ans = 0
for i in range(n): 
  if a[i]+i < n:
    x[a[i]+i] += 1
  if i-a[i] >= 0:
    ans += x[i-a[i]]
      
print(ans)