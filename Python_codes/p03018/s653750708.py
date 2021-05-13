s = input().replace("BC", "D")

ans = 0
cnt = 0
for i in s[::-1]:
    if i == "D":
        cnt += 1
    elif i == "A":
        ans += cnt
    else:
        cnt = 0



print(ans)