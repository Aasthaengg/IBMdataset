n = int(input())
s = list(input())

ans = 0

for i in range(n):
    a = set(s[:i])
    b = set(s[i:])
    ans = max(ans, len(a & b))

print(ans)