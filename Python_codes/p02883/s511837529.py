from math import ceil, cos
N,K=map(int,input().split())
A=list(map(int,input().split()))
F=list(map(int,input().split()))
A.sort()
F.sort(reverse=True)
sum_A = sum(A)
if K >= sum_A:
    print(0)
    exit()
AFC = [(A[i], F[i], A[i]*F[i]) for i in range(N)]
AFC.sort(key=lambda x: x[2])

def is_ok(x):
    rest = K
    #最大コストをx以下にできるか
    for i in range(N):
        a, f, cost = AFC[i]
        if cost <= x:
            continue
        need = ceil((cost - x)/f)
        rest -= need
    if rest >= 0:
        return True
    else:
        return False

left = 0
right = 10**12 + 100

while right-left > 1:
    mid = (left + right)//2
    res = is_ok(mid)
    if res:
        right = mid
    else:
        left = mid
print(right)