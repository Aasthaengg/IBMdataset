def main():
    M, K = list(map(int, input().split(' ')))
    if K >= 2 ** M:
        print(-1)
        return
    if M == 0:
        print('0 0')
        return
    if M == 1:
        if K == 0:
            print('0 0 1 1')
        else:
            print(-1)
        return
    # M >= 2 and K < 2 ** M
    arr = list(map(str, [i for i in range(2 ** M) if i != K]))
    rev_arr = arr.copy()
    rev_arr.reverse()
    ans = arr + [str(K)] + rev_arr + [str(K)]
    print(' '.join(ans))


if __name__ == '__main__':
    main()
