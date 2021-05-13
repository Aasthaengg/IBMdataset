import numpy as np
np
d = int(input())
c = [None] + list(map(int, input().split()))
s = [None] + [[None] + list(map(int, input().split())) for _ in range(d)]
t = [None] + [int(input()) for _ in range(d)]
last = np.zeros(27, dtype="i8")

satisfaction = 0
for i in range(1, d + 1):
    last += 1
    last[t[i]] = 0
    satisfaction += s[i][t[i]]
    for j in range(1, 27):
        satisfaction -= c[j] * (last[j])
    print(satisfaction)