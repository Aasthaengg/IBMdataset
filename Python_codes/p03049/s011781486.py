n = int(input())
ans = 0
a = 0
b = 0
ba = 0
for _ in range(n):
    s = input()
    if s[0] == 'B' and s[-1] == 'A':
        ba += 1
    else:
        if s[0] == 'B':
            b += 1
        if s[-1] == 'A':
            a += 1
    ans += s.count('AB')
t = ans
ans += ba - 1
if a >= 1:
    ans += 1
    a -= 1
if b >= 1:
    ans += 1
    b -= 1
ans += min(a, b)
print(max(ans, t))
