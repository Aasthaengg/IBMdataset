N = int(input())
A=list(map(int, input().split()))
from collections import Counter


c = Counter(A)
MOD = 10**9 + 7
if N % 2 == 0:
    is_ok = 1
    cnt = 0
    for num in range(1, N, 2):
        cnt += 1
        if c[num] != 2:
            is_ok=0
            break
    if not is_ok:
        print(0)
        exit()
    print(pow(2, cnt, MOD))
else:
    is_ok = 1
    cnt = 0
    if c[0] != 1:
        is_ok = 0
    for num in range(2, N, 2):
        cnt += 1
        if c[num] != 2:
            is_ok = 0
            break
    if not is_ok:
        print(0)
        exit()
    print(pow(2, cnt, MOD))