import sys


def main():
    N = int(input())

    for a in range(N // 4 + 1):
        for b in range(N // 7 + 1):
            if a * 4 + b * 7 == N:
                print("Yes")
                sys.exit()

    print("No")


if __name__ == "__main__":
    main()
