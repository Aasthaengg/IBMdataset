N, M, *AB = map(int, open(0).read().split())
AB = list(zip(*[iter(AB)]*2))

num = 0
cost = 0

for a, b in sorted(AB):
    if num+b >= M:
        cost += (M-num)*a
        break
    else:
        num += b
        cost += b*a

print(cost)