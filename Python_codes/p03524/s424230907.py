from collections import Counter
c = Counter(input())
labels = ['a', 'b', 'c']
min_cnt = min(c[label] for label in labels)
cnt = [c[label] - min_cnt for label in labels]
for x in cnt:
    if x in (0, 1):
        continue
    print('NO')
    break
else:
    print('YES')
