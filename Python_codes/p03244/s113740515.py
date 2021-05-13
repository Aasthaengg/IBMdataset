from collections import Counter


N = int(input())
V = list(map(int, input().split()))
V1 = []
V0 = []
for i, v in enumerate(V):
    if i % 2 == 0:
        V0.append(v)
    else:
        V1.append(v)

V1C = Counter(V1)
V0C = Counter(V0)
ans = 0

if V1C.most_common()[0][0] != V0C.most_common()[0][0]:
    ans = V1C.most_common()[0][1] + V0C.most_common()[0][1]
elif len(V1C) != 1 and len(V0C) != 1:
    ans = max(V1C.most_common()[1][1] + V0C.most_common()[0][1], V1C.most_common()[0][1] + V0C.most_common()[1][1])
elif len(V1C) != 1:
    ans = V1C.most_common()[1][1] + V0C.most_common()[0][1]
elif len(V0C) != 1:
    ans = V1C.most_common()[0][1] + V0C.most_common()[1][1]
else:
    ans = N // 2

print(N - ans)

