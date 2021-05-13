def main():
    n = int(input())
    k = int(input())
    xs = list(map(int, input().split()))
    ans = 0
    for x in xs:
        ax = x
        bx = k - x
        ans += min(ax*2, bx*2)
    print(ans)


if __name__ == "__main__":
    main()
