from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    counter = Counter(A)
    dupl_bars = [length for length, cnt in counter.items() if cnt > 1]
    dupl_bars.sort(reverse=True)
    if len(dupl_bars) > 1:
        if counter[dupl_bars[0]] > 3:
            print(dupl_bars[0] ** 2)
        else:
            print(dupl_bars[0] * dupl_bars[1])
    else:
        print(0)


if __name__ == '__main__':
    main()
