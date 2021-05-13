N = int(input())
A = [int(input()) for _ in range(N)]
cnt = 0
btn = 1
while(True):
    btn = A[btn-1]
    cnt += 1
    if btn == 2:
        print(cnt)
        break
    if cnt > 10**6:
        print(-1)
        break