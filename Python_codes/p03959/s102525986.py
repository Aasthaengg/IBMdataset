def main():
    n = int(input())
    t = list(map(int, input().split()))
    a = list(map(int, input().split()))

    is_certain, h = [0 for i in range(n)], t[:]
    is_certain[0] = 1
    for i in range(1, n):
        if t[i] > t[i-1]:
            is_certain[i] = 1

    if is_certain[-1] and h[-1] != a[-1]:
        print(0)
        exit()
    else:
        h[-1] = a[-1]
        is_certain[-1] = 1

    for i in range(n-2, -1, -1):
        if a[i] > a[i+1]:
            if is_certain[i] and h[i] != a[i]:
                print(0)
                exit()
            else:
                h[i] = a[i]
                is_certain[i] = 1
        elif is_certain[i] and a[i] < h[i]:
            print(0)
            exit()
        else:
            h[i] = min(h[i], a[i])

    ans = 1
    for i in range(n):
        if not is_certain[i]:
            ans = ans * h[i] % 1000000007

    print(ans)


if __name__ == '__main__':
    main()
