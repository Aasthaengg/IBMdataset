
def resolve():
    # P は [0, 1]
    N, P = map(int, input().split())
    A = list(map(int, input().split()))

    odds = sum([1 for a in A if a % 2 == 1])

    ans = 0
    if odds == 0:
        if P == 0:
            ans = 2 ** N
    else:
        ans = 2 ** (N - 1)

    print(ans)


if __name__ == "__main__":
    resolve()