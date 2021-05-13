a,b,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = min(a)+min(b)
for i in range(m):
  x,y,c = map(int,input().split())
  if count > a[x-1]+b[y-1]-c:
    count = a[x-1]+b[y-1]-c
    
print(count)