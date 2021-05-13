from collections import Counter

n, k = map(int, input().split())
a = input().split()
c = sorted(Counter(a).values(), reverse=True)

print(max(0, sum(c[k:])))