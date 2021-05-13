n, k = map(int, input().split())
td = sorted([list(map(int, input().split())) for i in range(n)], reverse=True, key=lambda x: x[1])

type = set()
L = []
Sum = 0
for x in td[:k]:
    Sum += x[1]
    if x[0] not in type:
        type.add(x[0])
    else:
        L.append(x[1])

L = L[::-1]
type_cnt = len(type)
ans = Sum + type_cnt ** 2
for x in td[k:]:
    if len(L)==0:break
    if x[0] not in type:
        type.add(x[0])
        type_cnt += 1
        Sum = Sum - L.pop(0) + x[1]
        ans = max(ans, Sum + type_cnt ** 2)
print(ans)
