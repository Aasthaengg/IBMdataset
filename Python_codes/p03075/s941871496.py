def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    nums = []
    nums.extend([a, b, c, d, e])
    nums.reverse()

    if (nums[0] - nums[4]) > k:
        print(':(')
    else:
        print('Yay!')

main()