s = input()
n = len(s) + 1

a = [-1] * n
tmp = 0

if s[0] == '<':
    a[0] = 0
if s[-1] == '>':
    a[-1] = 0

for i in range(1,n-2):
    if s[i] == '>' and s[i+1] == '<':
        a[i+1] = 0

for i in range(n-1):
    if a[i] == 0:
        tmp = 1
    else:
        tmp += 1
    if s[i] == '<':
        a[i+1] = tmp
    else:
        tmp = 0

for i in range(n-1):
    i = i * (-1) - 1
    if a[i] == 0:
        tmp = 1
    else:
        tmp += 1
    if s[i] == '>':
        a[i-1] = max(tmp, a[i-1])
    else:
        tmp = 0

print(sum(a))
