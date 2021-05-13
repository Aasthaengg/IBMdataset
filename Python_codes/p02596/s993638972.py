def main():
    k = int(input())
    if k & 0:
        print(-1)
        return

    r = 7 % k
    l = 0
    while r and l < k:
        r = (r * 10 + 7) % k
        l += 1

    print([l+1, -1][l == k])


if __name__ == '__main__':
    main()
