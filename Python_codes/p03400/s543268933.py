def resolve():
    '''
    code here
    '''
    N = int(input())
    D, X = [int(item) for item in input().split()]
    As = [int(input()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        day = 1
        while day <= D:
            day +=As[i] 
            cnt +=1

    print(cnt+X)


if __name__ == "__main__":
    resolve()
