import itertools

n, m = map(int, input().split())
xyz = []
for i in range(n):
    x, y, z = map(int, input().split())
    xyz.append((x, y, z))

bit = [-1, 1]
ret = 0
for i in itertools.product(bit, repeat=3):
    tmp = []
    for item in xyz:
        tmp.append(item[0] * i[0] + item[1] * i[1] + item[2] * i[2])
    tmp.sort()
    tmp.reverse()
    val = sum(tmp[:m])
    ret = max(ret, val)

print(ret)
