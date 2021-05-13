from typing import List


def main():
    nums = [int(n) for n in input().split()]

    print('Yes') if si(nums) else print('No')


def si(nums: List[int]) -> bool:
    a, b, c = nums

    if 4 * a * b < (c - a - b) ** 2 and (c - a - b) > 0:
        return True

    return False


if __name__ == '__main__':
    main()
