nums = list(map(int, input().split()))

M = max(nums)
while True:
    ans = 0
    for num in nums:
        ans += M - num
    if ans % 2 == 0:
        break
    M += 1

print(ans // 2)