s = list(input())
cf = ["C", "F"]
i = 0
for t in s:
    if t == cf[i]:
        i += 1
    if i == 2:
        break
print("Yes" if i == 2 else "No")