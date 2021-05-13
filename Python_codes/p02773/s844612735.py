from collections import Counter

n = int(input())
s = Counter()

for _ in range(n):
    s.update({input():1})

t = s.most_common()

ans = []
for item in t:
    if item[1] != t[0][1]:
        break
    ans.append(item[0])

ans = sorted(ans)

for i in ans:
    print(i)