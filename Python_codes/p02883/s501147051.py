N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
end = A[-1] * F[0] + 1
start = -1


def decision(n):
    k = K
    for a, f in zip(A, F):
        if a * f > n:
            k -= a - n // f
        if k < 0:
            return False
    return True

def calc():
    e = end
    s = start
    while e - s > 1:
        mid = (e + s)//2
        if decision(mid):
            e = mid
        else:
            s = mid
    return e


print(calc())