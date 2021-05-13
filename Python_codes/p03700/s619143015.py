import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort(reverse=True)
left = 0
right = 10**10
while left < right:
    mid = (left + right) // 2
    remaining = mid
    ok = True
    for health in h:
        x = (health-B*mid+A-B-1) // (A-B)
        remaining -= x
        if remaining < 0:
            ok = False
            break
    if ok:
        right = mid
    else:
        left = mid + 1
print(right)
