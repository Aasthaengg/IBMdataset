import sys

input = sys.stdin.readline


def main():
    X = int(input())

    ans = 0
    angle = 0
    while True:
        angle += X
        ans += 1
        if angle % 360 == 0:
            break
    print(ans)


if __name__ == "__main__":
    main()
