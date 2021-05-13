N = int(input())
S1 = input()
_ = input()
nums = [0]*N
ans = 3
c = 1
mod = 1000000007
for i in range(N-1):
    if S1[i] == S1[i + 1]:
        nums[i], nums[i + 1] = c,c
        c += 1

for i in range(N-1):
    if i > 0 and nums[i] == nums[i + 1] and nums[i] != 0 and nums[i - 1] != 0:
        ans *= 3 
    elif nums[i] == nums[i + 1] and nums[i] != 0:
        ans *= 2
    elif nums[i] == nums[i + 1] == 0:
        ans *= 2
    ans %= mod
print(ans)