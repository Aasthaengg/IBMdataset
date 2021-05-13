def main():
    nums = list(map(int, input().split()))

    M = max(nums)
    diff = 3 * M - sum(nums)

    print((diff) // 2) if diff%2 == 0 else print((3*M+3-sum(nums))//2)

if __name__ == '__main__':
    main()