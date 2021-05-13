N, M = map(int, input().split())
paths = [list(map(int, input().split())) for _ in range(M)]

minimumScore = [float('inf') for _ in range(N)]
minimumScore[0] = 0
for _ in range(N-1):
    flag = False
    for a, b, c in paths:
        c = -c
        if minimumScore[a-1] == -float('inf'):
            continue
        if minimumScore[a-1] + c < minimumScore[b-1]:
            minimumScore[b-1] = minimumScore[a-1] + c
            flag = True
    if not flag:
        break


negative = [False for i in range(N)]
for _ in range(N):
    for a, b, c in paths:
        c = -c
        if negative[a-1]:
            negative[b-1] = True
        if minimumScore[a-1] == -float('inf'):
            continue
        if minimumScore[a-1] + c < minimumScore[b-1]:
            negative[b-1] = True
            flag = True
if negative[-1]:
    print('inf')
else:
    print(-minimumScore[N-1])
#print(minimumScore[-1])
