s = input()

ans = 0
for a, b in zip(s, s[::-1]):
    if a != b:
        ans += 1

print(ans // 2)