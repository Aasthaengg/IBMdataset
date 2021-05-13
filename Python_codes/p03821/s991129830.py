import math
n = int(input())
a = []
b = []

for i in range(n):
    ai, bi = list(map(int, input().split()))
    a.append(ai)
    b.append(bi)

cur = 0

for i in range(n-1, -1, -1):
    res = (a[i]+cur)/b[i]
    if res % 1 == 0:
        continue

    rem = round((math.ceil(res) - res)*b[i])
    cur += rem

print(cur)