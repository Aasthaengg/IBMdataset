n = int(input())
nums = list(map(float, input().split(" ")))
res = 0
for i in range(n):
    res += (1/nums[i])
print(1/res)