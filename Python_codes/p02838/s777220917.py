from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
mod = pow(10,9) + 7
D = defaultdict(lambda:0)
for a in A:
    for i in range(61):
        D[1 << i] += bool(a & (1 << i))
ans = 0
for k, v in D.items():
    ans += k * (v * (n - v))
    ans %= mod
print(ans)