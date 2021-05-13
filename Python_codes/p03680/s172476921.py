N = int(input())
A = [int(input()) for _ in range(N)]
Pushed = [False]*N
Pushed[0] = True
i = 0
cnt = 0
while True:
    i = A[i] - 1
    cnt += 1
    if Pushed[i]:
        print(-1)
        break
    Pushed[i] = True
    if i == 1:
        print(cnt)
        break
