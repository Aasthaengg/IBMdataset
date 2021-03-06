import array
import bisect


def answer(n: int) -> int:
    numbers = array.array('L')

    i = 0
    while 100 ** i <= n:
        start = 100 ** i
        stop = int('9' * len(str(start))) + 1
        numbers.extend(range(start, stop))
        i += 1

    return bisect.bisect_right(numbers, n)


def main():
    n = int(input())
    print(answer(n))


if __name__ == '__main__':
    main()
