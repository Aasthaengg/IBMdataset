import math

s = input()
k = int(input())
cnt = 0
memo = 0
flg = True
if len(s) == 1:
    cnt = math.floor(k / 2)
elif len(set(s)) == 1:
    cnt = math.floor(len(s) * k / 2)
else:
    for i in range(1, len(s)):
        if s[0] == s[i] and flg:
            memo += 1
        else:
            flg = False
        if s[i] == s[i - 1]:
            s = s[:i] + '#' + s[i + 1:]
            cnt += 1
    cnt *= k
    if s[0] == s[-1] and memo % 2 == 0:
        cnt += (k - 1)
print(cnt)
