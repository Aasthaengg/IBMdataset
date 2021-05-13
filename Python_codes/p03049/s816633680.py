import sys

n, *s = sys.stdin.readlines()
a = 0
b = 0
ba = 0
ans = 0
for i in s:
    if i[0] == 'B' and i[-2] == 'A':
        ba += 1
    elif i[0] == 'B':
        b += 1
    elif i[-2] == 'A':
        a += 1
    ans += i.count('AB')
if a == 0 and b == 0 and ba > 0:
    ba -= 1
ans += ba + min(a, b)
print(ans)
