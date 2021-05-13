def main():
    N = int(input())
    a = sorted(map(int, input().split()))[::-1]
    diff = sum(a[::2]) - sum(a[1::2])
    print(diff)


if __name__ == "__main__":
    main()