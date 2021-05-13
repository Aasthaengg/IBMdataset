n = int(input())
s = []
for i in range(n):
    s.append(input())

cnt_end_a = 0
cnt_bgn_b = 0
cnt_end_a_bgn_b = 0

ans = 0
for i in range(n):
    if s[i][0] == 'B':
        if s[i][len(s[i])-1] == 'A':
            cnt_end_a_bgn_b += 1
        else:
            cnt_bgn_b += 1
    elif s[i][len(s[i])-1] == 'A':
        cnt_end_a += 1
    for j in range(len(s[i])-1):
        if s[i][j] == 'A' and s[i][j+1] == 'B':
            ans += 1

#print(cnt_end_a, cnt_bgn_b, cnt_end_a_bgn_b)

if cnt_end_a_bgn_b == 0:
    ans += min(cnt_bgn_b, cnt_end_a)
elif cnt_end_a == 0 and cnt_bgn_b == 0:
    ans += cnt_end_a_bgn_b - 1
elif cnt_end_a == 0:
    ans += cnt_end_a_bgn_b
elif cnt_bgn_b == 0:
    ans += cnt_end_a_bgn_b
else:
    ans += cnt_end_a_bgn_b + min(max(cnt_bgn_b, cnt_end_a), min(cnt_bgn_b, cnt_end_a))
print(ans)