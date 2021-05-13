LI = lambda: list(map(int, input().split()))

N, X = LI()
L = LI()


def main():
    ans = 1
    d = 0
    for l in L:
        d += l
        if d > X:
            break
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
