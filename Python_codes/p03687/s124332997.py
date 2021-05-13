S = input().strip()

ans = float("inf")

for i in range(26):
    tmp = 0
    current = 0
    for s in S:
        if s == chr(ord('a') + i):
            tmp = max(tmp, current)
            current = 0
        else:
            current += 1

    tmp = max(tmp, current)
    ans = min(ans, tmp)

print(ans)

