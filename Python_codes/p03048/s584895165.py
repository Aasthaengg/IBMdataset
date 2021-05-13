R,G,B,N = map(int, input().split())
index = 0
ans = 0
for_sort = [R,G,B]
for_sort.sort()
r = for_sort[2]
g = for_sort[1]
b = for_sort[0]
while N >=0:
  mid = N
  N -= r
  while mid >= 0:
    if mid % b == 0:
      ans += 1
    mid -= g
      
print(ans)    