def resolve():
    n = int(input())
    MOD = 10**9+7
    S = list(map(int, input().split()))

    if n % 2 == 0:
        sn = (1 + (n-1)) * (n // 2)
    else:
        sn = (2 + (n-1)) * (n//2)

    ss = sum(S)

    print((2**(n//2))%MOD if ss == sn else 0)

if __name__ == '__main__':
    resolve()