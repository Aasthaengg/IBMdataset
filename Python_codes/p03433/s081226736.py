url = "https://atcoder.jp/contests/abc088/tasks/abc088_a"

def main():
    n = int(input())
    m = int(input())

    ans = n % 500
    if ans <= m:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()


