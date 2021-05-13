
def resolve():
    N, K = map(int, input().split())

    A = [0] * K
    # a % K を決め打つと b % K, c % K のとるべき値が一意に決まることを利用します
    for i in range(1, N + 1):
        A[i % K] += 1

    res = 0
    for a in range(K):
        b = (K - a) % K
        c = (K - a) % K
        if (b + c) % K != 0:
            continue
        res += A[a] * A[b] * A[c]

    print(res)


if __name__ == "__main__":
    resolve()