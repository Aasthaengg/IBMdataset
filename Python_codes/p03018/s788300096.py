# https://atcoder.jp/contests/agc034/tasks/agc034_b

s = input()
s = s.replace('BC', 'X')
ans = 0
a = 0
for i in range(len(s)):
    if s[i] == 'A':
        a += 1
    elif s[i] == 'X':
        ans += a
    else:
        a = 0
print(ans)