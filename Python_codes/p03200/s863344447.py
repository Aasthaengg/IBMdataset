s = input()
count = 0
ans = 0
for i in s:
    if i == "W":
        ans += count
    else:
        count += 1
print(ans)