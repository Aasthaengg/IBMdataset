N = int(input())
s = [input() for i in range(N)]

cnt = 0
ab_cnt = 0
b_cnt = 0
a_cnt = 0
for word in s:
    cnt += word.count('AB')
    l = word[0]
    r = word[-1]
    if l == 'B' and r == 'A':
        ab_cnt += 1
    elif l == 'B':
        b_cnt += 1
    elif r == 'A':
        a_cnt += 1

if ab_cnt == 0:
    ans = min(b_cnt, a_cnt)
elif a_cnt + b_cnt > 0:
    ans = ab_cnt + min(b_cnt, a_cnt)
else:
    ans = ab_cnt - 1

print(cnt + ans)