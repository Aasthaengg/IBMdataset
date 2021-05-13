# AGC020A - Move and Win
def main():
    n, a, b = tuple(map(int, input().rstrip().split()))
    d = b - a - 1
    print("Alice" if d % 2 == 1 else "Borys")


if __name__ == "__main__":
    main()