a, b = input().split()

import math
if math.sqrt(int(a+b)) % 1== 0:
    print("Yes")
else:
    print("No")