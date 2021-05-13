s = input()
n = len(s)

ans = 0
for i in range(n):
    if s[i] == "g":
        ans += 1 if i % 2 == 1 else 0
    else:
        ans += -1 if i % 2 == 0 else 0

print(ans)
