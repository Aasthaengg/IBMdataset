def main():
    N = int(input())
    D = sorted(list(map(int, input().split())))
    a = D[N//2 - 1]
    b = D[N//2]
    ans = 0
    if a < b:
        ans = b - a
    print(ans)


if __name__ == '__main__':
    main()
