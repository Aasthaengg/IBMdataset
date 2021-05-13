N, K = map(int, input().split())
A = sorted(map(int, input().split()))
F = sorted(map(int, input().split()), reverse=True)


def ok(x):
    need = 0
    for i in range(N):
        need += max(0, A[i] - x // F[i])
    if need <= K:
        return True
    return False


left = -1
right = 10 ** 12 + 1

while right - left > 1:
    mid = (right + left) // 2
    if ok(mid):
        right = mid
    else:
        left = mid

print(right)