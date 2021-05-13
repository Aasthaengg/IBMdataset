H, W = map(int, input().split())
rl = [input() for _ in range(H)]

result = []
for i, r in enumerate(rl):
    result_r = ""
    pre_r = rl[i - 1] if i - 1 >= 0 else ""
    next_r = rl[i + 1] if i + 1 < H else ""
    for j, p in enumerate(r):
        if p == "#":
            result_r += "#"
            continue
        pre_j = j - 1 if j - 1 >= 0 else 0
        next_j = j + 2
        around_str = pre_r[pre_j:next_j] + r[pre_j:next_j] + next_r[pre_j:next_j]
        result_r += str(around_str.count("#"))
    result.append(result_r)

print("\n".join(result))

