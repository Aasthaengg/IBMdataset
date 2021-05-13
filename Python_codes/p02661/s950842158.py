N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

lb = sorted(v for v, _ in X)
ub = sorted(v for _, v in X)

if N % 2 == 0:
    l = lb[N // 2 - 1] + lb[N // 2]
    u = ub[N // 2 - 1] + ub[N // 2]
    print(u - l + 1)
else:
    l = lb[N // 2]
    u = ub[N // 2]
    print(u - l + 1)