n = int(input())

nums = []
for i in range(4):
    nums.append([])
    for j in range(3):
        nums[i].append([])
        for k in range(10):
            nums[i][j].append(0)


for _ in range(n):
    b,f,r,v = map(int, input().split())
    nums[b-1][f-1][r-1] += v

for i, building in enumerate(nums):
    for floor in building:
        print('', ' '.join(map(str, floor)))
    if i != 3:
        print('#'*20)