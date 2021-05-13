
def resolve():
    N = int(input())

    P = []
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        P.append((a + b, i))

    P.sort(reverse=True)
    taka = 0
    aoki = 0
    for i, (diff, idx) in enumerate(P):
        if i % 2 == 0:
            taka += A[idx]
        else:
            aoki += B[idx]

    print(taka - aoki)


if __name__ == "__main__":
    resolve()