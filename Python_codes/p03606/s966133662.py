def resolve():
    N = int(input())
    LR = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        cnt += LR[i][1] - LR[i][0] + 1
    print(cnt)

            

if '__main__' == __name__:
    resolve()