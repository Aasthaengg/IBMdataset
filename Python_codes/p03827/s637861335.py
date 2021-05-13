n = int(input())
s = input()

x, ans = 0, 0
for c in s:
    x += 1 if c == 'I' else -1
    ans = max(ans, x)

print(ans)
