#!/usr/bin/env python3


def main():
    N = int(input())
    nums = range(1, N + 1)
    while True:
        nums = [i // 2 if i % 2 == 0 else 0 for i in nums]
        if sum(nums) == 1:
            print([i + 1 for i in range(N) if nums[i] == 1][-1])
            break
        elif sum(nums) == 0:
            print(len(nums))
            break


main()
