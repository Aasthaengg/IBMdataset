n, s = open(0).read().split()

n = int(n)

ans = 0
for i in range(n):
    ans = max(ans, len(set(s[:i])&set(s[i:])))

print(ans)