N = int(input())

def solve(N):
    seventyfour = [78,101]
    twentyfour = [28,54,100,101]
    fourteen = [16,30,60,91,101]
    four = [6,9,20,28,44,52,68,76,92,116]
    two = [4,6,10,14,22,26,34,38,46,58,62,74,82,86,94,106]
    lists = [two,four,fourteen,twentyfour,seventyfour]
    nums = []
    for lis in lists:
        for i,n in enumerate(lis):
            if N<n:
                nums.append(i)
                break
    ans = nums[1]*(nums[1]-1)//2*(nums[0]-2)+nums[2]*(nums[1]-1)+nums[3]*(nums[0]-1)+nums[4]
    return ans
print(solve(N))