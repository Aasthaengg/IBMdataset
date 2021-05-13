# https://atcoder.jp/contests/agc035/tasks/agc035_a
from collections import Counter

n = int(input())
nums = [int(i) for i in input().split()]
c = Counter(nums)

if sum(nums) == 0:
    print('Yes')
elif len(c) == 2:
    for k, v in c.items():
        if k == 0:
            if v != n // 3:
                print('No')
                break
        else:
            if v != n // 3 * 2:
                print('No')
                break
    else:
        print('Yes')
elif len(c) == 3:
    t = 0
    for k, v in c.items():
        if v != n // 3:
            print('No')
            break
        t ^= k
    else:
        if t:
            print('No')
        else:
            print('Yes')
else:
    print('No')