from collections import Counter
n, k = map(int, input().split())
a = map(int, input().split())
ca = Counter(a)
print(sum(sorted([w for q, w in ca.items()])[:-k]))