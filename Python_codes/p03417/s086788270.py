n, m = map(int, input().split())

import itertools
print(abs(m*n - ((n-1)*2 + (m-1)*2)))