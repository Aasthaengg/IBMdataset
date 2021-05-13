n = int(input())
s = input()
t = input()

ans = n * 2
for i in range(n):
    if s[n - i - 1:] == t[:i + 1]:
        ans = min(ans, n * 2 - (i + 1))
print(ans)
