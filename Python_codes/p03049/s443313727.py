n = int(input())
ans = 0
cnt_ba = 0
cnt_a = 0
cnt_b = 0
for _ in range(n):
    s = str(input())
    ans += s.count('AB')
    if s[-1] == 'A' and s[0] == 'B':
        cnt_ba += 1
    elif s[-1] == 'A':
        cnt_a += 1
    elif s[0] == 'B':
        cnt_b += 1
if n >= 2:
    if cnt_a == cnt_b == 0:
        ans += max(0, cnt_ba - 1)
    else:
        ans += min(cnt_a, cnt_b) + cnt_ba
print(ans)
