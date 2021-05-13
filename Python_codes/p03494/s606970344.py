from typing import List


def answer(n: int, a: List[int]) -> int:
    count = 1
    while all(i % 2 ** count == 0 for i in a):
        count += 1
    return count - 1


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(n, a))


if __name__ == '__main__':
    main()
