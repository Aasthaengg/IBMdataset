LI = lambda: list(map(int, input().split()))

A, B, C = LI()
K = int(input())


def main():
    l = [A, B, C]
    l.sort()
    l[-1] *= 2 ** K
    ans = sum(l)
    print(ans)


if __name__ == "__main__":
    main()
