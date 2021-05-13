import numpy as np

d = int(input())
c = list(map(int, input().split()))
s = np.array([list(map(int, input().split())) for _ in range(d)])
t = [int(input()) for _ in range(d)]

last_day = np.zeros(26, dtype=int)

score = 0
for i in range(1, d + 1):
    last_day[t[i - 1] - 1] = i
    minus = ((last_day - i) * c).sum()
    score += s[i - 1, t[i - 1] - 1] + minus
    print(score)