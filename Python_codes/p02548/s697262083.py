from math import ceil
ans = 0
n = int(input())
for a in range(1, n + 1):
    for b in range(a+1, n + 1):
        c = n - a * b
        if c > 0:
            ans += 2
        else:
            break
for a in range(1, ceil(n**0.5) + 1):
        c = n - a * a
        if c > 0:
            ans += 1
        else:
            break
print(ans)