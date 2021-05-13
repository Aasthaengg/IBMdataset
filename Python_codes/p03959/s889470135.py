MOD = int(1e9) + 7


def calc(N, T, A):
    highest = max(T)
    if highest != max(A):
        return 0
    l = T.index(highest)
    r = A.index(highest)
    if N - (l + r) <= 0:
        return 0
    elif N - (l + r) == 1:
        ans = 1
    else:
        free = N - (l + r) - 2
        ans = pow(highest, free, MOD)
    prev = 0
    for i in range(l):
        if T[i] == prev:
            ans = (ans * T[i]) % MOD
        prev = T[i]
    prev = 0
    for i in range(r):
        if A[i] == prev:
            ans = (ans * A[i]) % MOD
        prev = A[i]
    return ans


def main():
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))[::-1]
    ans = calc(N, T, A)
    print(ans)


if __name__ == "__main__":
    main()
