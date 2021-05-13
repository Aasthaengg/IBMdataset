from itertools import product

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
print(sum(all(sum(i[b - 1] for b in a[1:]) % 2 == x for a, x in zip(s, p)) for i in product((0, 1), repeat=n)))