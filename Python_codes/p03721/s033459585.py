# ABC061_C
N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB)

for i in range(N):
    K -= AB[i][1]
    if K <= 0:
        print(AB[i][0])
        break