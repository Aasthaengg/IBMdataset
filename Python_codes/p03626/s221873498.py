from collections import defaultdict
from collections import deque
mod = int(1e9+7)
N = int(input())
S1 = input()
S2 = input()

if N == 1:
    print(3)
    exit()

if S1[0] == S1[1]:
    ans = 6
    for i in range(2, N):
        if S1[i-1] == S1[i]:
            continue
        if S1[i] == S2[i]:
            if S1[i-1] == S2[i-1]:
                ans *= 2
                ans %= mod
            else:
                continue
        else:
            if S1[i-1] == S2[i-1]:
                ans *= 2
                ans %= mod
            else:
                ans *= 3
                ans %= mod
else:
    ans = 3
    for i in range(1, N):
        if S1[i-1] == S1[i]:
            continue
        if S1[i] == S2[i]:
            if S1[i-1] == S2[i-1]:
                ans *= 2
                ans %= mod
            else:
                continue
        else:
            if S1[i-1] == S2[i-1]:
                ans *= 2
                ans %= mod
            else:
                ans *= 3
                ans %= mod

print(ans)
