def c_name(a, b):
    x = '0'*(6-len(str(a)))
    y = '0'*(6-len(str(b)))
    return x + str(a) + y + str(b)

N, M = map(int,input().split())

C = []

for i in range(M):
    p, y = map(int,input().split())
    _ = [i, p, y]
    C.append(_)

C.sort(key=lambda x: (x[1],x[2]))

d = {}
tmp = C[0][1]
num = 0
for i in C:
    if i[1] == tmp:
        num += 1
        d[i[0]] = c_name(i[1],num)
    else:
        tmp = i[1]
        num = 1
        d[i[0]] = c_name(i[1],num)

ans = sorted(d.items())

for i in ans:
    print(i[1])
