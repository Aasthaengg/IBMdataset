import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

def binary_search(ng=0, ok=max(a)):
    if ok - ng < 2: return ok
    mid = (ok + ng) // 2
    cnt = 0
    for i in a:
        cnt += math.ceil(i / mid) - 1
    if cnt <= k:
        return binary_search(ng, mid)
    else:
        return binary_search(mid, ok)
print(binary_search())