x = [int(input()) for _ in range(6)]

import math

ans = math.ceil(x[0] / min(x[1:])) + 4
print(ans)
