S = input()
K = int(input())

cnt = K
ans = ''

for s in S:
    if s == 'a':
        ans += 'a'
    elif cnt >= 123 - ord(s):
        cnt -= 123 - ord(s)
        ans += 'a'
    else:
        ans += s

last = ans[-1]
last = chr((ord(last) - 97 + cnt) % 26 + 97)
print(ans[:-1] + last)
