s = input()
ans = 0
b = 0
for si in s:
    if si == "B":
        b += 1
    else:
        ans += b
print(ans)