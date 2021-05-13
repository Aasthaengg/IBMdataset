# https://atcoder.jp/contests/agc037/tasks/agc037_a

s = input()

ans = 0
pre = ''
cur = ''
for i in range(len(s)):
    pre += s[i]
    if pre != cur:
        ans += 1
        cur = pre
        pre = ''
print(ans)