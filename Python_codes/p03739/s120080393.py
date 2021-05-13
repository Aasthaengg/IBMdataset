def calc(sign, A):
    cumsum_A = [0 for _ in range(len(A))]
    cumsum_A[0] = A[0]
    for i in range(len(cumsum_A) - 1):
        cumsum_A[i + 1] = cumsum_A[i] + A[i + 1]
    ret, offset = 0, 0
    for a in cumsum_A:
        b = a + offset
        if sign * b <= 0:
            diff = sign - b
            offset += diff
            ret += abs(diff)
        sign *= (-1)
    return ret


def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    print(min([calc(1, A), calc(-1, A)]))


if __name__ == '__main__':
    main()