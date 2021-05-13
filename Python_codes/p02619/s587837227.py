D = int(input())
C = list(map(int, input().split()))
S = [tuple(map(int, input().split())) for _ in range(D)]
T = [int(input()) - 1 for _ in range(D)]
Z = 26

last = [-1] * Z
cnt = 0
for d, t in enumerate(T):
    last[t] = d
    up = S[d][t]
    down = sum(C[i] * (d - last[i]) for i in range(Z))
    cnt += up - down
    print(cnt)
