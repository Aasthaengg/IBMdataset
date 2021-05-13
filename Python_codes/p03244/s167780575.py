# https://atcoder.jp/contests/abc111/tasks/arc103_a
from collections import Counter
n = int(input())
nums = [int(i) for i in input().split()]

odd = Counter(nums[1::2]).most_common()
even = Counter(nums[::2]).most_common()
odd.append((0, 0))
even.append((0, 0))
if odd[0][0] != even[0][0]:
    ans = n - (odd[0][1] + even[0][1])
else:
    s = n - (odd[0][1] + even[1][1])
    t = n - (odd[1][1] + even[0][1])
    ans = min(s, t)
print(ans)
'''
6
1 1 1 1 2 1
'''