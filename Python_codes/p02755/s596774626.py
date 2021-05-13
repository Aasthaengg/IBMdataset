a, b = map(int, input().split())

import math
flag = True
for i in range(1009):
    if math.floor(i * 0.08) == a and math.floor(i * 0.10) == b:
        print(i)
        flag = False
        break
if flag:
    print(-1)
