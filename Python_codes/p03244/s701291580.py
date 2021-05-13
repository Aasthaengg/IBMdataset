from collections import Counter

n = int(input())
v = list(map(int, input().split()))

v1 = v[0::2]
v2 = v[1::2]

c1 = Counter(v1)
c2 = Counter(v2)

c1 = c1.most_common()
c2 = c2.most_common()

if c1[0][0] != c2[0][0]:
    ans = n - c1[0][1] - c2[0][1]
else:
    if len(c2) > 1:
        choice_1 = c1[0][1] + c2[1][1]
    else:
        choice_1 = c1[0][1]
    if len(c1) > 1:
        choice_2 = c2[0][1] + c1[1][1]
    else:
        choice_2 = c2[0][1]
    ans = n - (max(choice_1, choice_2))

print(ans)