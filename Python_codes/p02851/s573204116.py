# int(input()) # 入力が1つ
from collections import defaultdict
n, k = map(int, input().split()) # 入力が複数
nums = [int(i) for i in input().split()] # 配列で数字

nums = [0] + nums
for i in range(n):
    nums[i + 1] = (nums[i] + nums[i + 1] + k - 1) % k
ans = 0
d = defaultdict(int)
for i in range(n + 1):
    ans += d[nums[i]]
    d[nums[i]] += 1
    if i - (k - 1) >= 0:
        d[nums[i - (k - 1)]] -= 1
print(ans)
