n = int(input())

count = 0

i = 1

count = 0
limit = 100

nums = [0] * n

for x in range(limit):
    for y in range(limit):
        for z in range(limit):
            cal =  (x + 1) ** 2 + (y + 1) ** 2 + (z + 1) ** 2 + (x + 1) * (y + 1) + (y + 1) * (z + 1) + (z + 1) * (x + 1)
            if(cal > n):
                break
            nums[cal - 1] += 1

for n in nums:
    print(n)