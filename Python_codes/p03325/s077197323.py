def main():
    N = int(input())

    ans = 0
    for x in map(int, input().split()):
        while x % 2 == 0:
            x //= 2
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
