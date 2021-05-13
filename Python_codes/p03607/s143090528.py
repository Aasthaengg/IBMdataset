n = int(input())
d = dict()
for _ in range(n):
    a = int(input())
    d.setdefault(a, -1)
    d[a] *= -1

ans = 0    
for k, v in d.items():
    if v == 1:
        ans += 1
print(ans)
