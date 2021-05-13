s = input()
ans = 0
for c in s:
    ans += 1 if c == "+" else -1
print(ans)
