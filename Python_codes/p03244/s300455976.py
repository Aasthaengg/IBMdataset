import collections
n = int(input())
v = list(map(int,input().split()))
v1 = []
v2 = []
for i in range(n):
    if i % 2 == 0:
        v1.append(v[i])
    else:
        v2.append(v[i])
c1 = collections.Counter(v1)
c2 = collections.Counter(v2)
c1Common = c1.most_common(2)
c2Common = c2.most_common(2)
answer = 0
if c1Common[0][0] != c2Common[0][0]:
    c1Count = n // 2 - c1Common[0][1]
    c2Count = n // 2 - c2Common[0][1]
    answer = c1Count + c2Count
else:
    c1Count = n // 2 - c1Common[0][1]
    c2Count = n // 2 - c2Common[0][1]
    if len(c1Common) > 1:
        c1Count2 = n // 2 - c1Common[1][1]
    else:
        c1Count2 = n // 2
    if len(c2Common) > 1:
        c2Count2 = n // 2 - c2Common[1][1]
    else:
        c2Count2 = n // 2
    case1 = c1Count + c2Count2
    case2 = c2Count + c1Count2
    if case1 < case2:
        answer = case1
    else:
        answer = case2
print(answer)