n=int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])
ab = sorted(ab, key=lambda x: x[1])

memo = 0
flag = True
for a,b in ab:
    memo += a
    if b < memo:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')