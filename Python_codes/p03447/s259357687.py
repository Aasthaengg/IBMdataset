#from typing import List


def input_nums():
    # type: () -> List[int]
    return list(map(int, open(0)))


def calc_nums(l):
    # type: (List[int]) -> int
    x, a, b = l
    return (x - a) % b


def main():
    # type () -> None:
    print(calc_nums(input_nums()))


if __name__ == '__main__':
    main()