LI = lambda: list(map(int, input().split()))

P, Q, R = LI()


def main():
    ans = min(P + Q, Q + R, R + P)
    print(ans)


if __name__ == "__main__":
    main()
