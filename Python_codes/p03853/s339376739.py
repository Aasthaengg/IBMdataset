h, w = map(int, input().split())

res = []
for _ in range(h):
    c = input()
    res.append(c)
    res.append(c)

for c in res:
    print(c)