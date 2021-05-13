from functools import reduce
from operator import xor
M, K = map(int, input().split())
if M == 1 and K == 1:
    print(-1)
elif not K:
    print(*(list(range(2**M)) + list(range(2**M))[::-1]))
elif not 0 <= K <= 2**M -1:
    print(-1)
else:
    T = [i for i in range(2**M) if i != K]
    if K != reduce(xor, T):
        print(-1)
    else:
        print(*([K] + T + [K] + T[::-1]))
