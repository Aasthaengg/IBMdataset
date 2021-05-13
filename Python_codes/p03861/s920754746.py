nums = [int(e) for e in input().split()]
def f(n, x):
    if n >=0:
        return int(n//x)+1
    elif n==-1:
        return 0

print(f(nums[1], nums[2])-f(nums[0]-1, nums[2]))
