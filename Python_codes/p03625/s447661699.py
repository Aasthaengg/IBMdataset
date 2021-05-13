n =int(input())
a = list(map(int,input().split()))
a.sort()
x,y,i = 0,0,0
while i<n:
  if a[i-1] == a[i]:
    x,y = y,a[i]
    i += 1
  i += 1
print(x*y)
