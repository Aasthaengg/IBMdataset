def main():
    A, B, C = map(int, input().split())
    nums = [A, B, C]
    nums.sort()
    ans = nums[2]*10 + nums[1] + nums[0]
    print(ans) 
main()