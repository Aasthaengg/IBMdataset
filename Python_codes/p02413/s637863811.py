r, c = map(int, input().split())
MAP = [[] for _ in range(r)]
for i in range(r):
    MAP[i].extend(list(map(int, input().split())))
    MAP[i].append(sum(MAP[i]))
    print(*MAP[i])
li = []
for Z in zip(*MAP):
    li.append(sum(Z))
print(*li)
