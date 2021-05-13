# https://atcoder.jp/contests/abc070/tasks/abc070_c
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))


def gcd(x, y):
    x, y = max(x, y), min(x, y)
    if y == 0:
        return 0
    if x % y == 0:
        return y
    return gcd(x % y, y)

ans = nums[0]
for num in nums:
    ans = ans * num // gcd(ans, num)
print(ans)
