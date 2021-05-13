N = int(input())
nums = list(map(int,input().split()))
ans = []
for _ in range(N):
    ma = -1
    ma_ind = -1
    l = len(nums)

    for i in range(l):
        if nums[i] == i + 1:
            ma_ind = i
    if ma_ind == -1:
        print(-1)
        exit(0)
    temp = nums.pop(ma_ind)
    ans.append(temp)
ans.reverse()
print("\n".join(map(str,ans)))