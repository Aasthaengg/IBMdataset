from typing import List


def main():
    n = int(input())
    nums = input().split(' ')
    r = don(n, nums)
    if r:
        print('YES')
    else:
        print('NO')


def don(n: int, nums: List[str]) -> bool:
    s = set()
    result = True

    for i in range(n):
        num = nums[i]
        if num in s:
            result = False
            break
        s.add(num)

    return result


if __name__ == '__main__':
    main()
