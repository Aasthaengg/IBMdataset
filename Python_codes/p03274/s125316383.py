N, K = map(int, input().split())
l = list(map(int, input().split()))

is_zero = l.count(0)
K -= is_zero

if K:
    ans = float('inf')
    for i in range(N-K+1):
        lb, rb = l[i], l[i+K-1]
        steps = abs(rb-lb) + min(abs(rb), abs(lb))
        ans = min(ans, steps)

    print(ans)
else:
    print(0)