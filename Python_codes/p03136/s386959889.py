t = int(input())
a = list(map(int,input().split()))
lon = max(a)
a.remove(lon)
k = sum(a)

if lon < k :
  print("Yes")
else :
  print("No")