N = int(input())
nums = [int(e) for e in input().split()]
nums.sort()
checker = nums[0]
count = 1
for i in range(1,N):
    if(checker != nums[i]):
        count+=1
        checker = nums[i]
if(N - count)%2==0:
    print(count)
else:
    print(count-1)