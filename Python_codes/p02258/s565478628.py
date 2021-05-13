def main():
    n = int(input())

    nums = []
    for i in range(n):
        nums.append(int(input()))

    rj = max(nums[1:])
    r  = rj - nums[0]

    for i in range(1, n-1):
        ri = nums[i]

        if ri == rj:
            rj = max(nums[i+1:])

        r = max(r, rj-ri)

    print(r)

if __name__ == '__main__':
    main()