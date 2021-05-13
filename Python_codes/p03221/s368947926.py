N, M = map(int, input().split())
data = [list(map(int, input().split())) + [_] for _ in range(M)]
data = sorted(data, key=lambda x: (x[0], x[1]))

order = 1
for i in range(M):
    if not i == 0 and not data[i][0] == data[i-1][0]:
        order = 1
    data[i].append(str(data[i][0]).zfill(6) + str(order).zfill(6))
    order += 1

data = sorted(data, key=lambda x: (x[2]))
for x in data:
    print(x[3])
