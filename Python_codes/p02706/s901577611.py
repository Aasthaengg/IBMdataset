# N: 夏休みの日数，M: 宿題の数
N, M = list(map(int, input().split()))
# i番目の宿題にかかる日数
A = list(map(int, input().split()))

free_days = N - sum(A)

if (free_days >= 0):
    print(free_days)
else :
    print(-1)