from itertools import product

n, m = map(int, input().split())
k = []
s = []
for _ in range(m):
    a, *b = map(int, input().split())
    k.append(a)
    s.append(b)
p = list(map(int, input().split()))
print(sum(all(sum(i[b - 1] for b in a) % 2 == x for a, x in zip(s, p)) for i in product((0, 1), repeat=n)))