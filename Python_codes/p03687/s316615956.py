s = list(input())
ans = len(s)
for c in set(s):
    dist = 0
    dists = []
    for d in s:
        if c != d:
            dist += 1
        else:
            dists.append(dist)
            dist = 0
    ans = min(ans, max(dists + [dist]))
print(ans)