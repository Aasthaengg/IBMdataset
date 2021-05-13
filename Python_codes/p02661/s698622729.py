
N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

lb = sorted(v for v, _ in X)
ub = sorted(v for _, v in X)
mid = N // 2
if N % 2 == 1:
    print(ub[mid] - lb[mid] + 1)
else:
    ans = (ub[mid - 1] + ub[mid]) - (lb[mid - 1] + lb[mid]) + 1
    print(ans)
