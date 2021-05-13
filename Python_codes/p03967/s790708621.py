from collections import Counter
s = list(input())
lens = len(s)
cs = Counter(s)

gp = cs["g"] - cs["p"]

print(gp // 2)