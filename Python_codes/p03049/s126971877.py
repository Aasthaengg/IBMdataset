n = int(input())

ans, ba, a, b = 0, 0, 0, 0

for i in range(n):
    s = input()
    ans += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        ba += 1
    elif s[-1] == 'A':
        a += 1
    elif s[0] == 'B':
        b += 1

if a > 0 and b > 0 and ba > 0:
    ans += ba + 1 + min(a-1, b-1)
elif a == 0 and b == 0:
    ans += max(ba-1, 0)
elif (a > 0 or b > 0) and ba > 0:
    ans += ba
elif ba == 0:
    ans += min(a, b)

print(ans)
