candidates = []
seps = ["KIH", "B", "R", ""]
for i in range(1 << 4):
    has_A = []
    for j in range(4):
        if i >> j & 1:
            has_A.append("A")
        else:
            has_A.append("")
    candidate = []
    for a, sep in zip(has_A, seps):
        candidate.append(a + sep)
    candidates.append("".join(candidate))

print("YES") if input() in candidates else print("NO")
