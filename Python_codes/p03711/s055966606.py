#!python3

LI = lambda: list(map(int, input().split()))

# input
x, y = LI()


def group(num):
    if num == 2:
        return 0
    if num in {4, 6, 9, 11}:
        return 1
    return 2


def main():
    if group(x) == group(y):
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
