n = int(input())
for i in range(0, n):
    nums = list(map(int, input().split()))
    max_num = max(nums)
    nums.remove(max_num)
    if max_num**2 == nums[0]**2 + nums[1]**2:
        print("YES")
    else:
        print("NO")
