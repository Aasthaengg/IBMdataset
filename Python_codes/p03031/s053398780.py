from itertools import product

n, m = map(int, input().split())
sp = [list(map(int, input().split())) for _ in range(m + 1)]
print(sum(all(sum(i[a - 1] for a in s[1:]) % 2 == p for s, p in zip(sp[:m], sp[-1])) for i in product((0, 1), repeat=n)))