order = list(map(len, input().split("T")))
x, y = map(int, input().split())
ans = "No"
lon = [order[i] for i in range(len(order)) if i % 2 == 0]
lat = [order[i] for i in range(len(order)) if i % 2 == 1]
x -= lon[0]
lon = lon[1:]
def f(x, A):
  A.append(abs(x))
  A.sort(reverse=True)
  k = A[0]
  for p in A[1:]:
      if k > 0:
        k -= p
      else:
        k += p
  if k == 0:
    return True
  else:
    return False
  
#print(lon, lat)
if f(x, lon) == f(y, lat) == True:
  ans = "Yes"
  
print(ans)