import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b = map(int, input().split())
_min, _max = min(a, b), max(a, b)
prime_factors = []
i = 2
while i ** 2 <= _min:
    ext = 0
    while _min % i == 0:
        ext += 1
        _min //= i
    if ext:
        prime_factors.append((i, ext))
    i += 1
if _min != 1:
    prime_factors.append((_min, 1))

ans = 1
for pf, _ in prime_factors:
    if _max % pf == 0:
        ans += 1
print(ans)
