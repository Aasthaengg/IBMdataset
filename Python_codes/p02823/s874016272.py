def main():
    N, A, B = list(map(int, input().split(' ')))
    assert 1 <= A < B <= N
    if (B - A) % 2 == 0:
        print((B - A) // 2)
    else:
        if B - 1 <= N - A:
            print(A + max([0, B - A - 1]) // 2)
        else:
            print(N - B + 1 + max([0, B - A - 1]) // 2)


if __name__ == '__main__':
    main()