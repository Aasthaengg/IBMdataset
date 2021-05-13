# yahoo-procon2019-qualB - Path
from collections import Counter
from itertools import chain


def main():
    P = [list(map(int, input().rstrip().split())) for _ in range(3)]
    C = Counter(chain.from_iterable(P)).most_common()
    c = [i[1] for i in C]
    print("YES" if c == [2, 2, 1, 1] else "NO")


if __name__ == "__main__":
    main()