from collections import Counter
n, *v = map(int, open(0).read().split())
vo = Counter(v[::2])
ve = Counter(v[1::2])
vomc = vo.most_common() + [(0, 0)]
vemc = ve.most_common() + [(0, 0)]
if vomc[0][0] == vemc[0][0]:
    ans = min(n//2 - vomc[0][1] + n//2 - vemc[1][1], n//2 - vomc[1][1] + n//2 - vemc[0][1])
else:
    ans = n//2 - vomc[0][1] + n//2 - vemc[0][1]
print(ans)