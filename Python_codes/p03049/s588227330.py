n = int(input())
ret = 0
cnt_ab = 0
cnt_a = 0
cnt_b = 0

for i in range(n):
    s = input()
    ret += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        cnt_ab += 1
    elif s[0] == 'B':
        cnt_b += 1
    elif s[-1] == 'A':
        cnt_a += 1

if cnt_ab == 0:
    ret += min(cnt_a, cnt_b)
else:
    if cnt_a + cnt_b > 0:
        ret += cnt_ab + min(cnt_a, cnt_b)
    else:
        ret += (cnt_ab - 1)


print(ret)
