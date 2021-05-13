
def main():
    x, y = map(int, input().split())
    if x % y != 0:
        print(abs((x // y + 1) - (x // y)))
    else:
        print(abs((x // y) - (x // y)))


if __name__ == "__main__":
    main()
