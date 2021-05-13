def main(A, B, C):
    if A + B < C:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    A, B, C = list(map(int, input().strip().split(' ')))
    main(A, B, C)