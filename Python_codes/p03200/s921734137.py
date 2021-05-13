S = input()[::-1]
ans = 0
cnt = 0
for s in S:
    if s == "W":
        cnt += 1
    else:
        ans += cnt
print(ans)
