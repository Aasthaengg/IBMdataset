from functools import reduce
from collections import Counter


N = int(input())
a = list(map(int, input().split()))
if N % 3 and a != [0] * N:
    print("No")
    exit()

nums = Counter(a)
ks = sorted(nums)
vs = sorted(nums.values())
if (
    (len(nums) == 1 and ks[0] == 0)
    or (len(nums) == 2 and ks[0] == 0 and vs[0] == N // 3)
    or (
        len(nums) == 3
        and all(v == N // 3 for v in vs)
        and reduce(lambda x, y: x ^ y, ks) == 0
    )
):
    print("Yes")
else:
    print("No")
