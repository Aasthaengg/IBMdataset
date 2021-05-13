import numpy as np
n = int(input())

aab = []

for i in range(n):
    a, b = map(int, input().split())
    aab.append([a + b, a, b])

aab.sort(reverse=True)
aab = np.array(aab)

a = aab[:, 1][0::2].sum()
b = aab[:, 2][1::2].sum()

print(a - b)