#!python3

# input
R = int(input())


def main():
    if R < 1200:
        ans = "ABC"
    elif R < 2800:
        ans = "ARC"
    else:
        ans = "AGC"
    print(ans)


if __name__ == "__main__":
    main()
