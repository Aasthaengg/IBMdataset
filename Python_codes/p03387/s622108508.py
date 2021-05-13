def main():
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)

    cnt = 0
    if (nums[1] - nums[2]) % 2 == 0:
        cnt += (nums[1] - nums[2]) // 2
        cnt += nums[0] - nums[1]

    else:
        cnt += 1
        cnt += (nums[1] - nums[2] + 1) // 2
        cnt += nums[0] - nums[1]

    print(cnt)

if __name__ == '__main__':
    main()
