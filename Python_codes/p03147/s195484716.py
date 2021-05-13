def main():
    N = int(input())
    h = list(map(int, input().split())) + [0]
    ans = 0; conti = False
    for line in range(1, 101):
        for i in range(N+1):
            if h[i] >= line and conti:
                continue
            elif h[i] >= line and not conti:
                conti = True
                ans += 1
            elif h[i] < line and conti:
                conti = False
            elif h[i] < line and not conti:
                continue
            else:
                pass

    print(ans)

if __name__ == "__main__":
    main()
