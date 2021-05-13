nums = [int(w) for w in input().split()]

nums.sort()
ans = 0
if (nums[1]-nums[0]) % 2 == 1:
    nums[0] -= 1
    ans += 1

ans += (nums[1]-nums[0])//2
ans += nums[2]-nums[1]
print(ans)
