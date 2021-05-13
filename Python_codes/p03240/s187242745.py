n = int(input())
xyhn = [None] * n
for i in range(n):
    xyhn[i] = list(map(int, input().split(' ')))

def calc_h(cx, cy, xyh):
    return xyh[2] + abs(cx - xyh[0]) + abs(cy - xyh[1])

base = -1
for i in range(n):
    if xyhn[i][2] != 0:
        base = i
        break

ans = None
for cx in range(0, 101):
    for cy in range(0, 101):
        result = True
        tmp_h = calc_h(cx, cy, xyhn[base])
        for k in range(n):
            if xyhn[k][2] > 0 and tmp_h != calc_h(cx, cy, xyhn[k]):
                result = False
                break
            if xyhn[k][2] == 0 and abs(cx - xyhn[k][0]) + abs(cy - xyhn[k][1]) < tmp_h:
                result = False
                break
        if result:
            ans = [cx, cy, calc_h(cx, cy, xyhn[base])]
            break

print(' '.join(map(str, list(ans))))

