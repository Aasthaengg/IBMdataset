def main():
    n = int(input())
    ts = list(map(int, input().split()))
    m = int(input())
    pxs = [list(map(int, input().split())) for _ in range(m)]

    for px in pxs:
        ans = 0
        for i in range(n):
            if i+1 == px[0]:
                ans += px[1]
            else:
                ans += ts[i]
        print(ans)


if __name__ == "__main__":
    main()
