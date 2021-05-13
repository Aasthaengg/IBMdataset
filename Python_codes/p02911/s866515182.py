def resolve():
    '''
    code here
    '''
    N, M, Q = [int(item) for item in input().split()]
    As = [int(input()) for _ in range(Q)]

    memo = [0 for _ in range(N)]

    for item in As:
        memo[item-1] += 1

    for item in range(N):
        if M - Q + memo[item] > 0:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    resolve()

