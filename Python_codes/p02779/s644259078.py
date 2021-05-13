from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
d = sorted(list(c.values()))
print('YES' if d[-1] == 1 else 'NO')