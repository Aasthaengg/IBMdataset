def answer(a: int, b: int, c: int, k: int) -> int:
    nums = sorted((a, b, c))
    nums[-1] = nums[-1] * 2 ** k

    return sum(nums)


def main():
    a, b, c = map(int, input().split())
    k = int(input())
    print(answer(a, b, c, k))


if __name__ == '__main__':
    main()
