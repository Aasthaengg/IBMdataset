def main():
    a,b,c = map(int, input().split())
    nums = []
    nums.append(a + b)
    nums.append(a + c)
    nums.append(b + c)
    nums.sort()
    print(nums[0])
main()