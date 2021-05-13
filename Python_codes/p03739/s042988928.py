n = int(input())
A = tuple(map(int, input().split()))

# 最左をプラスとする場合
sa = A[0]
pc = 0
if sa <= 0:
    pc = 1 - sa
    sa = 1
plus = -1
for a in A[1:]:
    sa += a
    if plus > 0 and sa <= 0:
        pc += 1 - sa
        sa = 1
    elif plus < 0 and sa >= 0:
        pc += 1 + sa
        sa = -1
    plus *= -1

# 最左がマイナスの場合
sa = A[0]
mc = 0
if sa >= 0:
    mc = 1 + sa
    sa = -1
plus = 1
for a in A[1:]:
    sa += a
    if plus > 0 and sa <= 0:
        mc += 1 - sa
        sa = 1
    elif plus < 0 and sa >= 0:
        mc += 1 + sa
        sa = -1
    plus *= -1

print(min(pc, mc))
