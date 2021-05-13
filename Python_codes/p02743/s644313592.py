from typing import List


def main():
    nums = [int(n) for n in input().split(' ')]

    if si(nums):
        print('Yes')
    else:
        print('No')


def si(nums: List[int]) -> bool:
    result = False
    a, b, c = nums

    if 4 * a * b < (c - a - b) ** 2 and (c - a - b) > 0:
        result = True

    return result


if __name__ == '__main__':
    main()
