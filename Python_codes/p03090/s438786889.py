n = int(input())
nums = list()
answers = list()
i = 0
if n % 2 == 0:
    while not(i == n / 2):
        nums.append((i+1,n-i))
        i += 1
else:
    while not(i == (n-1)/2):
        nums.append((i+1, n-i-1))
        i += 1
    nums.append((n,))
i = 0
while i < len(nums) - 1:
    for a in nums[i]:
        for b in nums[i+1]:
            answers.append((a, b))
    i += 1
if len(nums) >= 3:
    for a in nums[0]:
        for b in nums[-1]:
            answers.append((a,b))
print(len(answers))
for a, b in answers:
    print(a, b)
