N, *_XYH = map(int, open(0).read().split())
XYH = list(zip(*[iter(_XYH)]*3))

C = [(x, y) for x in range(101) for y in range(101)]

for c in C:
    for i, xyh in enumerate(sorted(XYH, key=lambda x: x[2], reverse=True)):
        if i==0:
            H = xyh[2] + abs(xyh[0] - c[0]) + abs(xyh[1] - c[1])
        elif max(H - abs(xyh[0] - c[0]) - abs(xyh[1] - c[1]), 0) == xyh[2]:
            is_ans = True
        else:
            is_ans = False
            break
        
    if is_ans:
        break

print(*c, H)