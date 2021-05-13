n = int(input())

a, b, ab = [], [], []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    ab.append(ai + bi)
ab.sort(reverse=True)

ans = -sum(b)
for i in range(0, n, 2):
    ans += ab[i]
print(ans)
