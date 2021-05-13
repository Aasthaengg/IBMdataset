def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        C_A = list(map(int, input().split()))
        C.append(C_A[0])
        A.append(C_A[1:])

    prices = []
    for bit in range(1 << N):
        price = 0
        understandings = [0] * M
        for i in range(N):
            if bit & (1 << i):
                price += C[i]
                for idx, a in enumerate(A[i], start=0):
                    understandings[idx] += a
        if min(understandings) >= X:
            prices.append(price)

    if len(prices) == 0:
        print(-1)
    else:
        print(min(prices))


if __name__ == '__main__':
    main()
