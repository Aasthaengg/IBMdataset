n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
a.append(0)
c = 0
d = 0
for spot in a:
  c += abs(d-spot)
  d = spot
for i in range(1,n+1):
  p = c-abs(a[i]-a[i-1])-abs(a[i]-a[i+1])+abs(a[i-1]-a[i+1])
  print(p)