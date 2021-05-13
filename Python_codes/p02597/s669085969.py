n = int(input())
c = list(input())

w = 0
r = c.count('R')
ans = max(w, r)
for i in range(n):
    if c[i] == 'W':
        w += 1
    else:
        r -= 1
    ans = min(ans, max(w, r))
print(ans)
