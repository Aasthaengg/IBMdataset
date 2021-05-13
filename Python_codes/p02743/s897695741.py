import math
a, b, c = map(int, input().split())
cab = c - a - b
if (cab > 0) and (4 * a * b < cab ** 2):
    print("Yes")
else:
    print("No")
