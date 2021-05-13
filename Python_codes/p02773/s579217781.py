from collections import Counter
n = int(input())
s = [str(input()) for i in range(n)]
s = Counter(s).most_common()
w = []
for h in s:
    if s[0][1] == h[1]:
        w.append(h[0])
w.sort()
for j in w:
    print(j)