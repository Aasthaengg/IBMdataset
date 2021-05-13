N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse = True)

def count_train(x):
    tmp = 0
    for a, f in zip(A, F):
        tmp += max(0, a - (x // f))
        if tmp > K:
            return tmp
    return tmp

ng = -1
ok = 10 ** 18
while ok - ng > 1:
    mid = (ok + ng) // 2
    if count_train(mid) <= K:
        ok = mid
    else:
        ng = mid

print(ok)