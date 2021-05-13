s = input()
b_count = 0
ans = 0
for i in range(len(s)):
    if s[i] == "B":
        b_count += 1
    else:
        ans += b_count
print(ans)
