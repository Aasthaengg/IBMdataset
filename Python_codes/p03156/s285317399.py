n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

nums = [0] * 3
for e in p:
    if e <= a:
        nums[0] += 1
    elif e <= b:
        nums[1] += 1
    else:
        nums[2] += 1

ans = min(nums)
print(ans)
