def check(A, F, K, x):
    for i in range(len(A)):
        if A[i] * F[i] > x:
            need = (A[i] * F[i] - x + F[i] - 1) // F[i]
            if need > K:
                return False
            K -= need
    return True


N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
F = list(map(int, input().split(' ')))
A.sort()
F.sort()
F = F[::-1]

high, low = 10 ** 13, -1
while high - low > 1:
    mid = (high + low) // 2
    if check(A, F, K, mid):
        high = mid
    else:
        low = mid
print(high)