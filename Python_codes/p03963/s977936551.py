def resolve():
    import sys
    input = sys.stdin.readline

    n, k = [int(x) for x in input().rstrip().split(" ")]

    print(k * ((k - 1) ** (n - 1)))


if __name__ == "__main__":
    resolve()
