how_many = int(input())
least, biggest = [],[]
for i in range(how_many):
    nums = input().split()
    nums = [int(num) for num in nums]
    least.append(nums[0])
    biggest.append(nums[1])
least.sort()
biggest.sort()
if how_many % 2 == 1:
    print(biggest[int((how_many-1) / 2)] - least[int((how_many-1) / 2)] + 1)
else:
    l = (least[int(how_many / 2)] + least[int(how_many / 2 - 1)]) / 2
    b = (biggest[int(how_many / 2)] + biggest[int(how_many / 2 - 1)]) / 2
    print(int((b-l) / 0.5 + 1))