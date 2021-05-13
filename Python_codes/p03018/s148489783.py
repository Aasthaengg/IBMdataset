s = input()
ans = 0
cnt = 0
idx = len(s)

while idx >= 0:
    if s[idx - 2 : idx] == "BC":
        cnt += 1
        idx -= 2
    elif s[idx - 1 : idx] == "A":
        ans += cnt
        idx -= 1
    else:
        idx -= 1
        cnt = 0

print(ans)
