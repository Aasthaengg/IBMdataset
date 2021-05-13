s = input()
ans = 0
now = 0
for i in s:
    if i == "B":
        now += 1
    else:
        ans += now
print(ans)