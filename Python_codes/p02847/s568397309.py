import sys

input = sys.stdin.readline


def main():
    next_day = {
        "SAT": 1,
        "FRI": 2,
        "THU": 3,
        "WED": 4,
        "TUE": 5,
        "MON": 6,
        "SUN": 7,
    }

    S = input().rstrip()
    ans = next_day[S]
    print(ans)


if __name__ == "__main__":
    main()
