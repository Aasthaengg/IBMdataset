from typing import List


def main():
    n = int(input())
    nums = [input() for _ in range(n)]
    print(wae(n, nums))


def wae(n: int, nums: List[str]) -> int:
    s = set()

    for i in range(n):
        num = nums[i]
        if num in s:
            s.remove(num)
        else:
            s.add(num)

    return len(s)


if __name__ == '__main__':
    main()
