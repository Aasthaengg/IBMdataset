a = int(input())
value = list(map(int, input().split()[:a]))
cost = list(map(int, input().split()[:a]))
l = []
for v, c in zip(value, cost):
    if v - c > 0:
        l.append(v -c)
res = 0
for item in l:
    if item > 0:
        res += item
print(res)