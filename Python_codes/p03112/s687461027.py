from bisect import bisect_left

a, b, q = map(int, input().split())
S = []
T = []
X = []


def calc(x, a, b):
    return abs(a - b) + min(abs(x - a), abs(x - b))


for _ in range(a):
    S.append(int(input()))
for _ in range(b):
    T.append(int(input()))
for _ in range(q):
    x = int(input())

    basho1 = bisect_left(S, x)
    basho11 = min(basho1, a - 1)
    basho12 = basho11 - 1

    basho2 = bisect_left(T, x)
    basho21 = min(basho2, b - 1)
    basho22 = basho21 - 1
    ans = calc(x, S[basho11], T[basho21])
    ans = min(ans, calc(x, S[basho11], T[basho22]))
    ans = min(ans, calc(x, S[basho12], T[basho21]))
    ans = min(ans, calc(x, S[basho12], T[basho22]))
    print(ans)
