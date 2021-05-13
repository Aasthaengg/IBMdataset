n = int(input())
s = input()
w_cnt = [0] * (n + 2)
e_cnt = [0] * (n + 2)
for i in range(1, n + 1):
    if s[i - 1] == 'W':
        w_cnt[i] = 1 + w_cnt[i - 1]
    else:
        w_cnt[i] = w_cnt[i - 1]

for i in range(1, n + 1):
    if s[-i] == 'E':
        e_cnt[n + 1 - i] = 1 + e_cnt[n + 2 - i]
    else:
        e_cnt[n + 1 - i] = e_cnt[n + 2 - i]
ans = n
for i in range(1, n + 1):
    tmp = w_cnt[i - 1] + e_cnt[i + 1]
    ans = min(ans, tmp)

print(ans)
