#!python3

# input
A, B = list(map(int, input().split()))


def main():
    if A > 8 or B > 8:
        ans = ":("
    else:
        ans = "Yay!"
    print(ans)


if __name__ == "__main__":
    main()
