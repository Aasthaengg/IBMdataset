n = int(input())
a = list(map(int, input().split()))
nums = []
nums.append(a[0])
for i in range(1, n):
    if a[i] != a[i-1]:
        nums.append(a[i])
    else:
        continue
val = nums[0]
maxs = []
for j in range(1, len(nums)):
    if nums[j] > val:
        maxs.append(j)
    else:
        pass
    val = nums[j]
pos = 0
money = 1000
for idx in maxs:
    minVal = min(nums[pos:idx])
    stocks = money // minVal
    money = money - minVal * stocks + nums[idx] * stocks
    pos = idx
print(money)
