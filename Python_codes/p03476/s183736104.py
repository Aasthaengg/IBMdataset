def main():
    # エラトステネスのふるい
    MAX_NUM = 101010
    is_prime = [1 for _ in range(MAX_NUM)]
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, MAX_NUM):
        if not is_prime[i]:
            continue
        for j in range(i * 2, MAX_NUM, i):
            is_prime[j] = 0

    # 2017-like 数かどうか
    like2017 = [0 for _ in range(MAX_NUM)]
    for i in range(MAX_NUM):
        if i % 2 == 0:
            continue
        if is_prime[i] and is_prime[(i + 1) // 2]:
            like2017[i] = 1

    # 累積和
    cumsum = [0 for _ in range(MAX_NUM + 1)]
    for i in range(MAX_NUM):
        cumsum[i + 1] = cumsum[i] + like2017[i]

    Q = int(input())
    L = [None] * Q
    R = [None] * Q
    for i in range(Q):
        l, r = map(int, input().split())
        L[i] = l
        R[i] = r

    for i in range(Q):
        print(cumsum[R[i] + 1] - cumsum[L[i]])


if __name__ == "__main__":
    main()
