import math

while 1:
    n = int(raw_input())

    if n == 0:
        break

    nums = map(float, raw_input().split(" "))

    m = sum(nums) / float(n)
    std = 0

    for i in range(n):
        std += (nums[i] - m) ** 2

    print(math.sqrt(std / float(n)))