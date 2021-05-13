import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n = int(input().rstrip())
    dx = [int(x) for x in input().rstrip().split(" ")]
    d = dx[0]
    x = dx[1]

    ans = 0

    for i in range(n):
        a = int(input().rstrip())

        day_count = 0
        while True:
            day = day_count * a + 1

            if day > d:
                break
            ans += 1
            day_count += 1

    print(ans + x)


if __name__ == "__main__":
    resolve()
