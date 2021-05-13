x1, y1, x2, y2 = map(float, input().split())
import math
ans = math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))
print("{0:.8f}".format(ans))