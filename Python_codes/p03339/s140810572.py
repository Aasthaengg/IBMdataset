import numpy as np

N = int(input())
S = input()
left_W = 0
right_E = S.count("E")
ans = N

for i in range(N):
    if S[i] == "W":
        ans = min(ans, left_W+right_E)
        left_W += 1
    else:
        right_E -= 1
        ans = min(ans, left_W+right_E)

print(ans)

