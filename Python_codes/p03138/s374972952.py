N, K = map(int, input().split())

kb = 60

bits = [K]
for i in range(kb):
    if (1 << i) & K:
        bits.append((K & ~((1 << i) - 1)) - 1)


bit0_count = [0] * kb
bit1_count = [0] * kb

for A in map(int, input().split()):
    for i in range(kb):
        if A & (1 << i):
            bit1_count[i] += 1
        else:
            bit0_count[i] += 1

ans = 0
for k in bits:
    tmp = 0
    for i in range(kb):
        if k & (1 << i):
            tmp += max(bit0_count[i], bit1_count[i]) * (1 << i)
        else:
            tmp += bit1_count[i] * (1 << i)
        
    ans = max(ans, tmp)

print(ans)