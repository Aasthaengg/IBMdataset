x,y = map(int,input().split())
f = 0
while x*2<=y:
  x *= 2
  f += 1
print(f+1)