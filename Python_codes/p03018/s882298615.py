s = input()
s = s.replace("BC", "X")
cnt, ans = 0, 0
for i in s:
    if i == "A":
        cnt += 1
    elif i == "X":
        ans += cnt
    else:
        cnt = 0
print(ans)