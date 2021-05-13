import math

N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]


def check(x):
    cnt = 0
    for h in H:
        if h <= B * x:
            continue
        else:
            cnt += math.ceil((h - B * x) / (A - B))

    if cnt <= x:
        return True
    else:
        return False


lb = 0
ub = 10**15
while ub - lb > 1:
    mid = (lb + ub) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

ans = ub

print(ans)
