times = int(input())
i = 0
nums = []
while i < times:
    nums.append(list(map(int, input().split())))
    i += 1

count = 0
for num in nums:
    count += num[1] - num[0] + 1

print(count)