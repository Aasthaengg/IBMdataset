url = "https://atcoder.jp/contests/abc046/tasks/abc046_b"

def main():

    n, m = list(map(int, input().split()))
    count = (m - 1) ** (n - 1) * m
    print(count)


if __name__ == '__main__':
    main()


