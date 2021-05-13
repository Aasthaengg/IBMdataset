n, k = map(int, input().split())
s = input()

cnt_1 = 0
cnt_2 = 0
res = 0
for i in range(n-1):
    if s[i] == 'L' and s[i+1] == 'R':
        cnt_1 += 1
    elif s[i] == 'R' and s[i+1] == 'L':
        cnt_2 += 1
    else:
        res += 1

if min(cnt_1, cnt_2) < k:
    res += min(cnt_1, cnt_2) * 2
    if cnt_1 != cnt_2:
        res += 1
else:
    res += k * 2

print(res)