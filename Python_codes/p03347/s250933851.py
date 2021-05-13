n = int(input())
nums = [int(input()) for _ in range(n)]
if nums[0] != 0:
    print(-1)
    exit()

ans = 0
for i in range(1, n):
    if nums[i] - nums[i-1] > 1:
        print(-1)
        exit()
    if nums[i] == 0:
        continue
    if nums[i] - nums[i-1] == 1:
        ans += 1
    else:
        ans += nums[i]
print(ans)