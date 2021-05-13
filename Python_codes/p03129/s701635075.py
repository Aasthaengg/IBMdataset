def main(N, K):
    if K * 2 - 1 <= N:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    N, K = map(int, input().split(' '))
    print(main(N, K))
