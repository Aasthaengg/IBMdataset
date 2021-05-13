n = int(input())
h = list(map(int,input().split()))

highest = h[0]
for i in range(n-1):
  if h[i] <= h[i+1] and h[i]+1 >= highest:
    continue
  else:
    if h[i]-1 <= h[i+1] and h[i+1] >= highest:
      highest = h[i]-1
      continue
    else:
      print("No")
      exit()
print("Yes")