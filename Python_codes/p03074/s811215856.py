n, k = map(int, input().split())
s = input()
a = []

if s[0] == "0":
    a.append(0)

zero_cnt = 0
one_cnt = 0
for i in range(n):
    if s[i] == "0":
        zero_cnt += 1
        if one_cnt > 0:
            a.append(one_cnt)
            one_cnt = 0
    else:
        one_cnt += 1
        if zero_cnt > 0:
            a.append(-1 * zero_cnt)
            zero_cnt = 0

if zero_cnt > 0:
    a.append(-1 * zero_cnt)
elif one_cnt > 0:
    a.append(one_cnt)

if s[-1] == "0":
    a.append(0)

a_len = len(a)

cum = [0] * (a_len + 1)
for i in range(1, a_len + 1):
    cum[i] = cum[i - 1] + abs(a[i - 1])

ans = 0

for left in range(0, a_len + 1, 2):
    right = left + k * 2 + 1
    if right > a_len:
        right = a_len

    ans = max(ans, cum[right] - cum[left])

print(ans)

