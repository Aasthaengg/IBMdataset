# A - Kyu in AtCoder

late_table = [
    [400, 8],
    [600, 7],
    [800, 6],
    [1000, 5],
    [1200, 4],
    [1400, 3],
    [1600, 2],
    [1800, 1]
]


def kyu(late):
    for i in late_table:
        if late < i[0]:
            return i[1] + 1
    return 1


if __name__ == "__main__":
    late = int(input())
    print(kyu(late))
