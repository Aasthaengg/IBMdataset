L, R = map(int, input().split())

import sys
minimum = sys.maxsize
for i in range(L, min(L + 2019, R)):
  for j in range(i+1, min(i + 1 + 2019, R+1)):
    minimum = min(minimum, i * j % 2019)
print(minimum)