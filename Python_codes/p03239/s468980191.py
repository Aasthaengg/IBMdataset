import math
inf = float('inf')

n, t = map(int, input().split())
c_t = [list(map(int, input().split())) for i in range(n)]

min_c = inf
for i in c_t:
    if i[1] <= t:
        min_c = min(min_c, i[0])

if min_c == inf:
    print("TLE")
else:
    print(min_c)