from collections import Counter
abs = []
for i in range(3):
    ab = list(map(int, input().split()))
    abs.extend(ab)
c = Counter(abs)
if c.most_common(1)[0][1] <= 2:
    print("YES")
else:
    print("NO")
