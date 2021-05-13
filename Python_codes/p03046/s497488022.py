from operator import xor
from itertools import repeat

M, K = map(int, input().split())

if K >= 2 ** M:
    print(-1)
elif K == 0:
    print(*(i // 2 for i in range(2 ** (M + 1))))
else:
    if M == 1:
        print(-1)
    else:
        t = ([0] + list(reversed(range(1, 2 ** M))) + list(range(2 ** M)))
        print(*map(xor, t, repeat(K)))
