def main():
    N = int(input())
    S = list()
    pow_m2, mod = 1, 2
    S.append(N % mod)
    N -= (N % mod) * pow_m2
    while N != 0:
        pow_m2 *= (- 2)
        mod *= 2
        s = 1 if N % mod > 0 else 0
        S.append(s)
        N -= s * pow_m2
    S.reverse()
    print(''.join(map(str, S)))


if __name__ == '__main__':
    main()
