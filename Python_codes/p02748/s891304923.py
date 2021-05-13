A,B,M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = 10000000

for i in range(M):
  x,y,c = map(int, input().split())
  m= min(m, a[x-1]+b[y-1]-c)
  
m = min(m, min(a)+min(b))
  
print(m)