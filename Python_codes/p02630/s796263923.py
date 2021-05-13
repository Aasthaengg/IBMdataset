import collections

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

x = dict(collections.Counter(A))
ans = sum(k * v for k, v in x.items())
for _ in range(Q):
    B, C = map(int, input().split())
    b = x.get(B, 0)
    c = x.get(C, 0)

    ans -= b * B
    ans += b * C

    x[C] = c + b
    x[B] = 0

    print(ans)