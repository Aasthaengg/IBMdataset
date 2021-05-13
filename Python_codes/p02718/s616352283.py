def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0

    for i in A:
        if i/sum(A) >= 1/(4*M):
            cnt += 1
    if cnt >= M:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()