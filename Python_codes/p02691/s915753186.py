n = int(input())
a = tuple(map(int, input().split()))

plus = {}
minus = {}
for i in range(n):
    p = i + 1 + a[i]
    m = i + 1 - a[i]
    if p not in plus:
        plus[p] = 0
    if m not in minus:
        minus[m] = 0
    plus[p] += 1
    minus[m] += 1

cnt = 0
for i in plus.keys():
    if i in minus:
        cnt += plus[i]*minus[i]

print(cnt)