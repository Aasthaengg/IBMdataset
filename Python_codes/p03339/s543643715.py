n = int(input())
s = list(input())
ans = 1001001
wn = 0
en = sum([1 for i in s[1:] if i == 'E'])
for i in range(n):
    ans = min(ans, wn + en)
    if s[i] == 'W':
        wn += 1
    if i != n - 1:
        if s[i + 1] == 'E':
            en -= 1
print(ans)