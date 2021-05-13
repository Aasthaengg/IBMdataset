from collections import deque

n, k = map(int, input().split())
v = list(map(int, input().split()))

m = min(k, n)
res = 0
for A in range(0, m + 1):
    for B in range(0, m + 1):
        if A + B > m:
            continue
        if B == 0:
            L = v[:A]
        else:
            L = v[:A] + v[-B:]
        L.sort()
        L = deque(L)
        num = k - (A + B)
        for i in range(num):
            if len(L) == 0:
                continue
            elif len(L) == 1:
                if L[0] < 0:
                    L.pop()
            else:
                Remove = L.popleft()
                if Remove > 0:
                    L.appendleft(Remove)
        res = max(res, sum(L))

print(res)