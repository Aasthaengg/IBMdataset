import itertools
from statistics import mean

input = list(map(int, input().split()))
n = input[0]
m = input[1]
d = input[2]

if (d != 0):
    ans = (n - d) * 2 / (n ** 2) * (m - 1)
else:
    ans = (n - d) / (n ** 2) * (m - 1)

print(ans)
