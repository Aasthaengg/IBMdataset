s = input()
k = int(input())
d = {}
dd = {}
for i, ss in enumerate('abcdefghijklmnopqrstuvwxyz'):
    d[ss] = i
    dd[i] = ss
ans = ''

for ss in s[:-1]:
    if k >= 26 - d[ss] and ss != 'a':
        k -= 26 - d[ss]
        ans += 'a'
    else:
        ans += ss
k = (d[s[-1]] + k) % 26
ans += dd[k]
print(*ans, sep='')