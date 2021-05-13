# https://atcoder.jp/contests/abc072/tasks/arc082_b

n = int(input())
nums = [int(i) for i in input().split()]
t = 0
for i in range(n):
    if i == n - 1 and nums[i] == i + 1:
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
        t += 1
    elif nums[i] == i + 1:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        t += 1
print(t)