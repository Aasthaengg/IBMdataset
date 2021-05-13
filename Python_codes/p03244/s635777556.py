from collections import Counter
n = int(input())
v = list(map(int, input().split()))
v1 = [v[i] for i in range(n) if i % 2 == 0]
v2 = [v[i] for i in range(n) if i % 2 != 0]

c1 = Counter(v1)
c2 = Counter(v2)

c1 = sorted(c1.items(), key=lambda x:(x[1], -x[0]), reverse=True)
c2 = sorted(c2.items(), key=lambda x:(x[1], -x[0]), reverse=True)
ans = 0
if c1[0][0] != c2[0][0]:
    if len(c1) != 1:
        for k, v in c1[1:]:
            ans += v
    if len(c2) != 1:
        for k, v in c2[1:]:
            ans += v
    print(ans)
else:
    if len(c1) == 1 and len(c2) == 1:
        ans += n // 2
    elif len(c1) == 1 and len(c2) > 1:
        ans += len(v2) - c2[1][1]
    elif len(c1) > 1 and len(c2) == 1:
        ans += len(v1) - c1[1][1]
    else:
        if c1[1][1] < c2[1][1]:
            ans += len(v1) - c1[0][1]
            ans += len(v2) - c2[1][1]
        else:
            ans += len(v1) - c1[1][1]
            ans += len(v2) - c2[0][1]
    print(ans)
