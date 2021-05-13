# B - String Rotation
from collections import deque

S = deque(str(input()))
T = deque(str(input()))
N = len(S)
ans = 'No'

for _ in range(N):
    S.append(S.popleft())
    if S == T:
        ans = 'Yes'

print(ans)