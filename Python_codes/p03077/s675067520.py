n = int(input())
p = []
for _ in range(5):
    p.append(int(input()))
m = min(p)
idx = p.index(m)
ans = (idx - 1) + n // m + (5 - idx)
if n % m:
    ans += 1
print(ans)