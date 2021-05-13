def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        while True:
            if a % 2 == 1:
                break
            a /= 2
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
