MOD = 998244353


def main():
    N, S = map(int, input().split())
    A = list(sorted(map(int, input().split())))
    prev = [0] * (S+1)
    prev[0] = pow(2, N, MOD)
    half = pow(2, MOD-2, MOD) % MOD
    for i in range(N):
        cur = list(prev)
        for total in range(S+1):
            if total + A[i] > S:
                continue
#            key = encode(num+1, total + A[i], S)
            cur[total + A[i]] = (cur[total + A[i]] +
                                 prev[total] * half) % MOD
        prev = cur
    print(cur[S])


if __name__ == "__main__":
    main()
