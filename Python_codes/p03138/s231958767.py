def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    l = len(bin(max(max(A), K))) - 2
    L = [0] * l
    ans = 0
    k = 0
    for a in A:
        for j in range(l):
            if (a >> j) & 1 == 1:
                L[j] += 1
    for i, b in enumerate(L[::-1]):
        if b < N - b:
            if K >= k + 2 ** (l - i - 1):
                b = N - b
                k += 2**(l - i - 1)
        ans += b * (2**(l - i - 1))
    print(ans)


if __name__ == '__main__':
    main()