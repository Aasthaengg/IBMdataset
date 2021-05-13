def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]

    ab.sort(reverse=True, key=lambda x: x[0] + x[1])

    t = 0
    a = 0

    for i in range(0, n, 2):
        t += ab[i][0]
    for i in range(1, n, 2):
        a += ab[i][1]

    ans = t - a

    print(ans)


if __name__ == "__main__":
    main()
