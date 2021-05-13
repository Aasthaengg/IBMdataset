count = ans = 0
for idx, c in enumerate(input()):
    if c == "W":
        ans += idx - count
        count += 1
print(ans)