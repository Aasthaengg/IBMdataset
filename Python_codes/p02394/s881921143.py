W, H , x, y, r = map(int, raw_input().split())

if (0 <= x + r <= W) and (0 <= x - r <= W) and (0 <= y + r <= H) and (0 <= y - r <= H):
  print "Yes"

else:
  print "No"