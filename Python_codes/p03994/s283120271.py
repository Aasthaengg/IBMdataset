from string import ascii_lowercase

s = input()
k = int(input())

d = {c: (26 - i) % 26 for i, c in enumerate(ascii_lowercase)}

ret = ''
for c in s[:-1]:
    if d[c] <= k:
        k -= d[c]
        ret += 'a'
    else:
        ret += c

k %= 26
idx = (ascii_lowercase.index(s[-1]) + k) % 26
c = ascii_lowercase[idx]
ret += c

print(ret)
