import collections

n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

c = collections.Counter(a)

p = [k-q] * n
for i in list(c.keys()):
    p[i-1] += c[i]

for i in p:
    print('Yes' if i > 0 else 'No')