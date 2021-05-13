x = input()
total = 0
ans = 0
for s in x:
    if s == "T":
        total += 1
        ans = max(ans, total)
    else:
        total -= 1
print(ans * 2)