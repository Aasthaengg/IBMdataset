def resolve():
    '''
    code here
    '''
    N, x = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]
    As.sort()

    cnt = 0
    while x > 0 and cnt < N:
        x -= As[cnt]
        if cnt == N-1:
            if x == 0:
                cnt += 1
        else:
            if x >= 0:
                cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    resolve()
