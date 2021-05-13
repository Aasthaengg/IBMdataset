import math, re

x1, y1, x2, y2 = [float(n) for n in re.split(r"\s+", input().strip())]
print("%f" % (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)))

