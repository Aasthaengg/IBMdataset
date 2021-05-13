from itertools import accumulate


def main():
    creatures = int(input())
    size = [int(x) for x in input().split()]
    size.sort()
    accumulate_size = list(accumulate(size))
    survivable = 0
    for i in range(creatures - 1):
        if 2 * accumulate_size[i] < size[i + 1]:
            survivable = i + 1
    print(creatures - survivable)


if __name__ == '__main__':
    main()

