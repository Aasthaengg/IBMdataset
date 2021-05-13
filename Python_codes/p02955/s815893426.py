
"""
https://atcoder.jp/contests/abc136/tasks/abc136_e
"""

N, K = map(int, input().split())
X = list(map(int, input().split()))


def calc_divisor(x):
    divisor = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x // i:
                divisor.append(x // i)
    return divisor


divisor = calc_divisor(sum(X))
ans = 0
for v in divisor:
    cand = sorted(x % v for x in X)
    cs1 = [0] * (N + 1)
    for i in range(N):
        cs1[i + 1] = cs1[i] + cand[i]

    cs2 = [0] * (N + 1)
    for i in reversed(range(N)):
        cs2[i] = cs2[i + 1] + v - cand[i]

    for a, b in zip(cs1, cs2):
        if a <= K and a == b:
            ans = max(ans, v)
            break

print(ans)
