s = input()

ans, b = 0, 0
for i in s:
    if i == "B":
        b += 1
    else:
        ans += b

print(ans)

