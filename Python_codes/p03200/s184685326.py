s = input()
cnt = 0
ans = 0
for i in range(len(s)-1,-1,-1):
    if s[i] == "W":
        cnt += 1
    if s[i] == "B":
        ans += cnt
print(ans)