s = input()
rl = []
start = 0
for i in range(len(s)):
    if i == len(s) - 1 or s[i] == "L" and s[i + 1] == "R":
        rl.append(s[start: i + 1])
        start = i + 1

ans = [0] * len(s)
start = 0
for i in range(len(rl)):
    x = rl[i].index("L")
    ans[start + x] = x // 2 + (len(rl[i]) - x - 1) // 2 + 1
    ans[start + x - 1] = (x - 1) // 2 + (len(rl[i]) - x) // 2 + 1
    start += len(rl[i])
print(*ans)