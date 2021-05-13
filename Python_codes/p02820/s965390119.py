n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

use = [1]*n
for i in range(n-k):
    if not use[i]:
        continue
    if t[i] == t[i+k]:
        use[i+k] = 0

ans = 0
for i in range(n):
    if use[i]:
        x = t[i]
        if x == 'r':
            ans += p
        elif x == 's':
            ans += r
        else:
            ans += s
print(ans)
