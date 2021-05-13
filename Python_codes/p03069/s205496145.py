n = int(input())
s = input()
cnt_w, cnt_b = s.count("."), 0
ans = cnt_w
if s.count(".") == n or s.count("#") == n:
    ans = 0
else:
    for i in range(n):
        if s[i] == "#":
            cnt_b += 1
        else:
            cnt_w -= 1
        if i == n - 1 or s[i] != s[i + 1]:
            ans = min(ans, cnt_w + cnt_b)
print(ans)
