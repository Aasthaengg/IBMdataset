def main():
    n = int(input())
    # n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    while True:
        currentmin = 10**10
        currentminIndex = 0
        for i in range(n):
            if currentmin > a[i] and a[i] != 0:
                currentmin = a[i]
                currentminIndex = i
        for i in range(n):
            if i != currentminIndex:
                a[i] = a[i] % currentmin
        count = 0
        for i in range(n):
            if a[i] != 0:
                count += 1
        if count == 1:
            break

    print(max(a))


if __name__ == '__main__':
    main()

