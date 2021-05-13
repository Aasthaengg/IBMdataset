def main():
    K = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    if A[0] != 2:
        print(-1)
        return
    n = 2
    lower_n, upper_n = 2, 3
    for a in A:
        # [lower_n, upper_n]内にaの倍数が無ければNG
        if upper_n // a - (lower_n - 1) // a == 0:
            print(-1)
            return
        lower_n = (lower_n + a - 1) // a * a  # ceil(lower_n/a) * a
        upper_n = upper_n // a * a + a - 1  # # floor(upper_n/a) * a + a - 1
    print('{} {}'.format(lower_n, upper_n))


if __name__ == '__main__':
    main()