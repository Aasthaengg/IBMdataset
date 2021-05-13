def main():
    import sys

    MOD = 1000000007
    N, *A = map(int, sys.stdin.buffer.read().split())
    C = [0] * (N + 1)
    C[0] = 3
    ans = 1
    for a in A:
        ans = ans * C[a]
        C[a] -= 1
        C[a + 1] += 1

    print(ans % MOD)
    return


if __name__ == '__main__':
    main()
