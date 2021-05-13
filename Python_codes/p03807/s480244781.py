import collections


def main():
    _ = int(input())
    print("YES" if collections.Counter(list(map(lambda x: int(x) %
                                                2, list(map(int, input().split())))))[1] % 2 == 0 else "NO")


if __name__ == '__main__':
    main()
