from collections import Counter

E = []
for _ in range(3):
    a, b = map(int, input().split())
    E.append(a); E.append(b)
cnt = Counter(E)
print('YES' if max(cnt.values()) == 2 else 'NO')