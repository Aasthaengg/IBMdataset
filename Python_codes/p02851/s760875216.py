
from collections import deque
from collections import defaultdict


def p_e():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    for i in range(n):
        a[i + 1] = (a[i + 1] + a[i] - 1) % k
    d = defaultdict(int)
    d[0] = 1
    q = deque()
    ans = 0
    for i in range(1, n + 1):
        if i - k >= 0:
            d[a[i - k]] -= 1
        ans += d[a[i]]
        d[a[i]] += 1
    print(ans)
    
p_e()