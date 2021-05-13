n = int(input())
s, t = input(), input()
p = ''
i = 0
while i < n:
    if s[i] == t[i]:
        p += 'X'
    else:
        p += 'Y'
        i += 1
    i += 1
ans = (3 if p[0] == 'X' else 6)
for i in range(1, len(p)):
    if p[i] == 'X':
        if p[i - 1] == 'X':
            ans *= 2
        else:
            ans *= 1
    else:
        if p[i - 1] == 'X':
            ans *= 2
        else:
            ans *= 3
print(ans % (10 ** 9 + 7))