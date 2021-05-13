def resolve():
    N = int(input())
    A = [int(input()) - 1 for _ in range(N)]
    flgs = [False for _ in range(N)]
    flgs[0] = True
    i = A[0]
    flgs[i] = True
    cnt = 1
    while not flgs[1]:
        i = A[i]
        if flgs[i]:
            print(-1)
            return
        else:
            flgs[i] = True
            cnt += 1
    else:
        print(cnt)


resolve()
