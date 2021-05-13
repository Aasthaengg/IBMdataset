N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort(reverse=True)
F.sort()


def judge(x):
    val = 0
    for i in range(N):
        val += max(A[i] - x // F[i], 0)
        if val > K:
            return False
    if val <= K:
        return True


ub = 10**12
lb = -1

while lb + 1 < ub:
    x = (ub+lb)/2
    if judge(x):
        ub = x
    else:
        lb = x

print(int(ub))
