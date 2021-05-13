s = input()
cnt_b = 0
ans = 0
for c in s:
    if c == "B":
        cnt_b += 1
    else:
        ans += cnt_b

print(ans)
