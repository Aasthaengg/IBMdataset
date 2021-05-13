S = input()
ans = 0
cnt = 0

for s in S:
    if s in "AGCT":
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 0

ans = max(cnt, ans)

print(ans)