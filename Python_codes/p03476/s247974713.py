import numpy as np
q = int(input())
b = [True] * (10**5+1)
for i in range(2, 10**5):
    if not b[i]:
        continue
    x = 2 * i
    while x <= 10**5:
        b[x] = False
        x += i
b[0] = b[1] = False
a = [False] *  (10**5+1)
for i in range(1, 10**5, 2):
    if b[i] and b[int((i+1)/2)]:
        a[i] = True
cumsum = np.array(a).cumsum()
for _ in range(q):
    l, r = map(int, input().split())
    print(cumsum[r] - cumsum[l-1])