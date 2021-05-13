N, M = map(int, input().split(' '))

broken_list = []
if M > 0:
    for i in range(M):
        broken_list.append(int(input()))
        
broken_set =set(broken_list)
nums = [0] * (N + 1)
nums[0] = 1

if 1 not in broken_set:
    nums[1] = 1

for i in range(2, N + 1):
    nums[i] = nums[i - 1] + nums[i - 2]
    if i in broken_set:
        nums[i] = 0

print(nums[N] % 1000000007)