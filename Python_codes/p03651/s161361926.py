# https://atcoder.jp/contests/agc018/tasks/agc018_a

n, k = map(int, input().split())
nums = [int(i) for i in input().split()]

def gcd(x, y): #GCD
    # greatest_common_divisor
    if x < y:
        x, y = y, x
    if y == 0:
        return 0
    if x % y == 0:
        return y
    return gcd(y, x % y)

MAX = max(nums)
GCD = nums[0]
for num in nums:
    GCD = gcd(GCD, num)

if k <= MAX and k % GCD == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')