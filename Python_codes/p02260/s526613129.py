def main() :
    n = int(input())
    nums = [int(i) for i in input().split()]
    exchange_count = 0

    for i in range(n) :
        min_idx = nums[i:].index(min(nums[i:]))
        if nums[i] != nums[min_idx + i] :
            exchange_count += 1
        nums[i], nums[min_idx + i] = nums[min_idx + i], nums[i]

    print(" ".join(map(str, nums)))
    print(exchange_count)

if __name__ == '__main__' :
    main()