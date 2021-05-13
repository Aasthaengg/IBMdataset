import numpy as np

d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) - 1 for _ in range(d)]
last = np.zeros(26, dtype="i8")

satisfaction = 0
for i in range(d):
    last += 1
    last[t[i]] = 0
    satisfaction += s[i][t[i]]
    for j in range(26):
        satisfaction -= c[j] * (last[j])
    print(satisfaction)
