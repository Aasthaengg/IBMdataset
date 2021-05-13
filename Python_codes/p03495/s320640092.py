from  collections import Counter

n, k = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
values, counts = zip(*c.most_common())
print(n - sum(counts[:k]))