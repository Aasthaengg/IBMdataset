def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]

    ab.sort(reverse=True, key=lambda x: x[0] + x[1])

    t = sum(map(lambda x: x[0], ab[::2]))
    a = sum(map(lambda x: x[1], ab[1::2]))

    ans = t - a

    print(ans)


if __name__ == "__main__":
    main()
