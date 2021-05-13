def main():
    n, k = [int(e) for e in input().split()]
    V = [int(e) for e in input().split()]

    ans = 0
    vc = min(n, k)
    for vci in range(1, vc + 1):
        for vcii in range(vci + 1):
            Hand = []
            for li in range(vcii):
                Hand.append(V[li])

            for ri in range(vci - vcii):
                Hand.append(V[-ri - 1])

            Hand.sort()
            for i in range(min(k - vci, len(Hand))):
                if Hand[i] < 0:
                    Hand[i] = 0

            ans = max(sum(Hand), ans)

    print(ans)


if __name__ == '__main__':
    main()
