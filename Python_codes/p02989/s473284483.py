def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    half = n // 2
    print(d[half] - d[half - 1])


if __name__ == "__main__":
    main()