def read_values():
    return map(int, input().split())


def read_list():
    return list(map(int, input().split()))


def main():
    N, T = read_values()
    A = read_list()

    m = A[0]
    p = 0
    D = {}
    for a in A:
        if m > a:
            D[p - m] = D.setdefault(p - m, 0) + 1
            m = a
            p = a
        else:
            p = max(p, a)
    D[p - m] = D.setdefault(p - m, 0) + 1

    k = max(D.keys())
    print(D[k])


if __name__ == "__main__":
    main()
