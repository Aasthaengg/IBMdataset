n = int(input())
nums = sorted(map(int, input().split()))
if n % 2 == 0:
    if nums[::2] != nums[1::2]:
        print(0)
    else:
        print(2 ** (n // 2) % 1000000007)
else:
    if nums[0] == 0 and nums[1::2] == nums[2::2]:
        print(2 ** (n // 2) % 1000000007)
    else:
        print(0)