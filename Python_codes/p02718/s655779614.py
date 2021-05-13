n,m = map(int,input().split())
hyo = list(map(int,input().split()))
all_hyo = sum(hyo)

hyo.sort(reverse=True)

a = True

for x in range(m):
  if hyo[x] < all_hyo / 4 / m:
    a = False
    break

if a :
  print("Yes")
else:
  print("No")
