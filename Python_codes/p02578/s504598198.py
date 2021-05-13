def main():
    n = int(input())
    A = list(map(int, input().split()))
    s = 0
    ans = 0

    for a in A:
        if a > s:
            s = a
        else:
            ans += s - a

    print(ans)


if __name__ == '__main__':
    main()
