import numpy as np

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
next_ = 0
for i in range(N):
    num_monster = max(A[i] - next_, 0)
    if num_monster <= B[i]:
        ans += num_monster + min(next_, A[i])
        next_ = B[i] - num_monster
    else:
        ans += B[i] + min(next_, A[i]) 
        next_ = 0
ans += min(next_, A[N])

print(ans)
