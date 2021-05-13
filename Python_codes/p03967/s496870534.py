s = list(input())

ans = 0

for i in range(len(s)):
    ans += i & 1

for c in s:
    if c == 'p':
        ans -= 1

print(ans)