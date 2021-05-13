import math
N,C,K = list(map(int,input().split()))
T = sorted([int(input()) for _ in range(N)])
ans = 1
count = 0
first = T[0]
for t in T:
    if t <= first+K and count < C:
        count += 1
    else:
        count = 1
        ans += 1
        first = t
print(ans)