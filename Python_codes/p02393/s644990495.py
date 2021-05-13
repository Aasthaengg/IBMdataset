a, b, c = map(int, raw_input().split())

max = max(a,b)
min = min(a,b)
if max < c:
  middle = max
  max = c

elif min > c:
  middle = min
  min = c

else:
 middle = c

print "%d %d %d" %(min, middle, max)