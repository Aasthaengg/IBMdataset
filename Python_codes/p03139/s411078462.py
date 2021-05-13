# nikkei2019-qualA - Subscribers
def main():
    n, a, b = list(map(int, input().rstrip().split()))
    print(min(a, b), max(0, (a + b) - n))


if __name__ == "__main__":
    main()