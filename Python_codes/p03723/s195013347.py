def resolve():
    '''
    code here
    '''
    A, B, C = [int(item) for item in input().split()]
    cnt = 0

    while A%2 == 0 and B%2 == 0 and C%2 == 0:
        A, B, C = B//2 + C//2, A//2 + C//2, A//2 + B//2
        cnt += 1

        if A==B==C:
            cnt = -1
            break

    print(cnt)


if __name__ == "__main__":
    resolve()
