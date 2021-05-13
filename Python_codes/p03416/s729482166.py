a,b = map(int,input().split())
n = b - a + 1
count = 0

for i in range(n):
  x = a + i
  xx = list(str(x))
  xx.reverse()
  xx = int("".join(xx))
  if x == xx:
    count += 1
    
print(count)