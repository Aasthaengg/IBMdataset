def resolve():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    maxcnt = 0
    prev = H[0]
    for i in range(1, N):
        if prev >= H[i]:
            cnt += 1
        else:
            maxcnt = max(maxcnt, cnt)
            cnt = 0
        prev = H[i]
    maxcnt = max(maxcnt, cnt)
    print(maxcnt)

    
if '__main__' == __name__:
    resolve()