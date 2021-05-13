def main():
    N = int(input())
    *H, = map(int, input().split())

    ans = 0
    cnt = 0
    prev = H[0] - 1
    for h in H:
        if h <= prev:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
        prev = h

    print(ans)


if __name__ == '__main__':
    main()
