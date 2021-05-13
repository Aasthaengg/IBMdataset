from collections import defaultdict, deque

N, K = map(int, input().split())

neighbor = defaultdict(list)

for i in range(N-1):
    a, b = map(int, input().split())
    neighbor[a-1].append(b-1)
    neighbor[b-1].append(a-1)

d = deque([(0, -1)])

ans = K
mod = 10**9 + 7
while d:
    cur, par = d.pop()

    i = 1 if par == -1 else 2
    for n in neighbor[cur]:
        if n != par:
            d.append((n, cur))
            ans *= (K-i)
            ans %= mod
            i += 1

print(ans)