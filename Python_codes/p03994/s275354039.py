s = input()
k = int(input())
loop = ord('z') + 1
remaining = k
ans = []
for c in s:
    if c == 'a':
        ans.append(c)
        continue
    r = loop - ord(c)
    if r <= remaining:
        ans.append('a')
        remaining -= r
    else:
        ans.append(c)
if remaining > 0:
    remaining %= 26
    ans[-1] = chr(ord(ans[-1]) + remaining)
print(''.join(ans))
