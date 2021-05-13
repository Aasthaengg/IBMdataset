from collections import Counter
s = input()

cnt = list(Counter(s).values())
if len(cnt) < 3: cnt.append(0)
print('YES' if max(cnt) - min(cnt) <= 1 else 'NO')